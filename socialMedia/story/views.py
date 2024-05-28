from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Story
from .serializers import StorySerializer
from django.core.exceptions import ObjectDoesNotExist
from app.models import UserFollow
from django.utils import timezone
from datetime import timedelta

# Create your views here.

class StoryCreateView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        serializer=StorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        user=request.user
        stories=Story.objects.filter(user=user)
        serializer=StorySerializer(stories,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class StorydeleteView(APIView):
    permission_classes=[IsAuthenticated]
    def delete(self, request, pk):
        try:
            story = Story.objects.get(pk=pk, user=request.user)
        except Story.DoesNotExist:
            return Response({'error': 'Story not found or not authorized to delete'}, status=status.HTTP_404_NOT_FOUND)
        story.delete()
        return Response({'message': 'Story deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class StoryListView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        user=request.user
        following_user = UserFollow.objects.filter(user=user).values_list('follows', flat=True)
        stories=Story.objects.filter(user__in=following_user,created_at__gte=timezone.now() - timedelta(hours=24))
        serializer=StorySerializer(stories,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


