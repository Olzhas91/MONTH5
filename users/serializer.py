from rest_framework import serializers

from .models import User, UserCode


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)


class UserConfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCode
        fields = ('code',)
