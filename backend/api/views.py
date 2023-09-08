import random

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response

from .models import (
    Service,
    ServiceProfile,
    UserProfile,
    SimpleUserProfile,
    UserRequest,
    ServiceHashtag
)
from .serializers import (
    ServiceSerializer,
    ServiceProfileSerializer,
    SimpleUserProfileSerializer,
    UserRequestSerializer
)


# Create your views here.

class UserCreate(CreateAPIView):
    """
    Creates the user.
    """
    queryset = UserProfile.objects.all()


class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceCreate(CreateAPIView):
    queryset = ServiceProfile.objects.all()
    serializer_class = ServiceProfileSerializer


class SimpleUserProfileCreate(CreateAPIView):
    queryset = SimpleUserProfile.objects.all()
    serializer_class = SimpleUserProfileSerializer


class UserRequestCreate(CreateAPIView):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestSerializer


@api_view(['GET'])
def get_service_id_by_name(request, name):
    service = Service.objects.get(name=name)
    return JsonResponse({"service_id": service.pk})


@api_view(["GET"])
def get_service_name_by_id(request, service_id):
    service = Service.objects.get(pk=service_id)
    return JsonResponse({"service": service.name})


@api_view(["GET"])
def get_hashtags_by_service(request, service_id):
    service = Service.objects.get(pk=service_id)
    hashtags = [tag.name for tag in service.services.all()]
    return JsonResponse({"hashtags": hashtags})


@api_view(["POST"])
def generate_tags_for_service(request):
    data = dict(**request.data)
    print(data)
    service = Service.objects.get(pk=data['service_id'][0])
    print('asdfasasfd')
    for value in data['tags_list']:
        ServiceHashtag.objects.create(
            service=service, name=value
        )
    return JsonResponse({"status": "ok"})


@api_view(["GET"])
def get_service_profile_ids(request):
    service_profiles = ServiceProfile.objects.all()
    return JsonResponse({
        "service_profiles": [
            service_profile.telegram_chat_id for service_profile in service_profiles
        ]
    })


@api_view(["GET"])
def get_simple_users_chat_id(request):
    simple_users = SimpleUserProfile.objects.all()
    return JsonResponse({
        "simple_users": [
            simple_user.tg_chat_id for simple_user in simple_users
        ]
    })


@api_view(["POST"])
def generate_auth_code(request):
    data = request.data

    x = random.sample([f"{i}" for i in range(10)], 6)
    code = ''.join(x)

    try:
        service_profile = ServiceProfile.objects.get(phone_number=data["phone_number"])
        service_profile.verification_code = code
        service_profile.save()
    except Exception as e:
        print(e.__class__)
        return Response({"status": "No user with this phone number"})
    return Response({"status": "ok"})


@api_view(["POST"])
def check_verification_code(request, verification_code):
    user = ServiceProfile.objects.filter(verification_code=verification_code)
    if not user:
        return JsonResponse({"exists": False})
    return JsonResponse({'exists': True})
