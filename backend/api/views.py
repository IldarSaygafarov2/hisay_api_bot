from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Service, ServiceProfile
from .serializers import ServiceSerializer, ServiceProfileSerializer


# Create your views here.

class UserCreate(APIView):
    """
    Creates the user.
    """

    def post(self, request, format='json'):
        return Response('hello')


@api_view(["GET"])
def get_users_chat_id(request):
    return
    # users = UserProfile.objects.all()
    # return Response(users, many=True)


class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceCreate(CreateAPIView):
    queryset = ServiceProfile.objects.all()
    serializer_class = ServiceProfileSerializer

    # def post(self, request, *args, **kwargs):
    #     print(request.data, args, kwargs)
    #     return Response({'a': 'a'})


@api_view(['GET'])
def get_service_id_by_name(request, name):
    service = Service.objects.get(name=name)
    return JsonResponse({"service_id": service.pk})