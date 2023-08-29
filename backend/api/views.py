from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView

from .models import Service, ServiceProfile, UserProfile, SimpleUserProfile
from .serializers import ServiceSerializer, ServiceProfileSerializer, SimpleUserProfileSerializer


# Create your views here.

class UserCreate(CreateAPIView):
    """
    Creates the user.
    """
    queryset = UserProfile.objects.all()


@api_view(["GET"])
def get_users_chat_id(request):
    return


class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceCreate(CreateAPIView):
    queryset = ServiceProfile.objects.all()
    serializer_class = ServiceProfileSerializer


class SimpleUserProfileCreate(CreateAPIView):
    queryset = SimpleUserProfile.objects.all()
    serializer_class = SimpleUserProfileSerializer


@api_view(['GET'])
def get_service_id_by_name(request, name):
    service = Service.objects.get(name=name)
    return JsonResponse({"service_id": service.pk})


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