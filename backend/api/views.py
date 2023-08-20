from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile

# Create your views here.


@api_view(["GET"])
def get_users_chat_id(request):
    users = UserProfile.objects.all()
    return Response(users)
