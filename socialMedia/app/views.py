from app.serializers import UserRegistrationSerializer,UserLoginSerializer
from app.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



# for genetaing tokens
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserResistration(APIView):
    def post(self,request):
        serializer=UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            ##token=get_tokens_for_user(user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class UserLogin(APIView):
    def post(self,request):
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email=serializer.data['email']
            password=serializer.data['password']
            user=authenticate(email=email,password=password)
            if user:
                token=get_tokens_for_user(user)
                return Response({"token":token},status=status.HTTP_200_OK)
            else:
                return Response({"msg":"Login Failed"},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
