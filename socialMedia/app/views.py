from app.serializers import UserRegistrationSerializer,UserLoginSerializer,UserProfileSerializer,UserChangePasswordSerializer,UserFollowSerializer,UserProfileImageSerializer
from app.models import User,UserFollow,UserProfileImage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist

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
    


class UserProfile(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        serializer=UserProfileSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)




class UserChangePassword(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        serializer=UserChangePasswordSerializer(data=request.data,context={'user':request.user})
        if serializer.is_valid():
            return Response({"msg":"Password Change Successfully"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class UserFollowView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,pk):
        following=UserFollow.objects.filter(user=request.user)
        follower=UserFollow.objects.filter(follows=request.user)
        following_serializer=UserFollowSerializer(following,many=True)
        follower_serializer=UserFollowSerializer(follower,many=True)
        return Response({"Following":following_serializer.data,"Followers":follower_serializer.data},status=status.HTTP_200_OK)
    
    def post(self,request,pk):
        try:
            following_user=User.objects.get(pk=pk)
            #serializer=UserFollowSerializer
            follow_user=UserFollow.objects.get_or_create(user=request.user,follows=following_user)
            if not follow_user[1]:
                follow_user[0].delete()
                return Response({"msg":"Unfollowed user"},status=status.HTTP_200_OK)
            else:
                return Response({"msg":"Followed user"},status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({"error": "User not Exist"}, status=status.HTTP_404_NOT_FOUND)
        


class ProfileImageUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user_profile_image = UserProfileImage.objects.get(user=request.user)
        except UserProfileImage.DoesNotExist:
            user_profile_image = UserProfileImage(user=request.user)
        
        serializer = UserProfileImageSerializer(user_profile_image, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)