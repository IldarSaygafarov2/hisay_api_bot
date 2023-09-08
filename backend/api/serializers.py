from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import UserProfile, Service, ServiceProfile, SimpleUserProfile, UserRequest


class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRequest
        fields = (
            "chat_id",
            "title",
            "body",
            "username",
            "service",
            "location"
        )


class ServiceProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProfile
        fields = ("first_name",
                  "last_name",
                  "surname",
                  "document_photo",
                  "kind_of_activity",
                  "telegram_chat_id",
                  "service",
                  )


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=UserProfile.objects.all())]
    )
    phone_number = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=UserProfile.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=UserProfile.objects.all())]
    )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
            phone_number=validated_data['phone_number'],
        )
        return user

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email', 'password', 'phone_number')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("id", "name")


class SimpleUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleUserProfile
        fields = ("tg_username", "fullname", "tg_chat_id", "phone_number")
