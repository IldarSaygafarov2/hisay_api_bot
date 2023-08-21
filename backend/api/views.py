from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserProfile

# Create your views here.

class UserCreate(APIView):
    """
    Creates the user.
    """

    def post(self, request, format='json'):
        return Response('hello')


@api_view(["GET"])
def get_users_chat_id(request):
    users = UserProfile.objects.all()
    return Response(users)
