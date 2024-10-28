from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']


    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class UserLoginSerializer(serializers.Serializer):


    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self):
        user = authenticate(
            email=self.validated_data['email'],
            password=self.validated_data['password'])

        if user is None:
            raise serializers.ValidationError('Invalid credentials')

        return user
