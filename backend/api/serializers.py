from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import UserProfile


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
