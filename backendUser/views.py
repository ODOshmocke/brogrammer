from django.contrib.auth import login
from django.shortcuts import render
from .models import User
from .serializers import UserSerializer, UserRegisterSerializer, UserLoginSerializer

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.



class



class UserRegisterAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLoginAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()
        if user is None:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(password):
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)

        responseData = {
            "id": user.id,
            "name": user.username,
            "email": user.email,
            "password": serializer.data['password'],
            "is_staff": user.is_staff,
        }

        return Response(responseData, status=status.HTTP_200_OK)

