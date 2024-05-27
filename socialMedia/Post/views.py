from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from Post.serializers import PostSerializer,PostCommentSerializer,PostLikeSerializer
from Post.models import Post,PostLike,postComment
from django.core.exceptions import ObjectDoesNotExist



class PostView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        serializer=PostSerializer(data=request.data,context={'request': request})

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        user=request.user
        posts=Post.objects.filter(user=user)
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class PostDetailView(APIView):
    permission_classes=[IsAuthenticated]
    def put(self,request,pk):
        post = Post.objects.get(pk=pk,user=request.user)
        serializer = PostSerializer(post, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = Post.objects.get(pk=pk,user=request.user)
        post.delete()
        return Response({"msg":"post deleted"},status=status.HTTP_204_NO_CONTENT)
    

class UserPostsByPkView(APIView):
    permission_classes=[IsAuthenticated]
    def get_user_posts(self, pk):
        try:
            return Post.objects.filter(user_id=pk)  
        except Post.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        user_posts = self.get_user_posts(pk)
        serializer = PostSerializer(user_posts, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class LikePostView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request,pk):
        try:
            post=Post.objects.get(id=pk)
            new_like_post=PostLike.objects.get_or_create(user=request.user,post=post)
            if not new_like_post[1]:
                new_like_post[0].delete()
                return Response({"msg":"Post Unliked"},status=status.HTTP_200_OK)
            else:
                return Response({"msg":"Post liked"},status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    def get(self,request,pk):
        try:
            post = Post.objects.get(id=pk)
            likes=PostLike.objects.filter(post=post)
            serializer = PostLikeSerializer(likes,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)




class PostCommentView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request,pk):
        try:
            post = Post.objects.get(id=pk)
            data = request.data
            data['post'] = post
            serializer = PostCommentSerializer(data=data,context={'request': request})
            if serializer.is_valid():
                serializer.save(post=post)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
        
    
    def get(self,request,pk):
        try:
            post = Post.objects.get(id=pk)
            comments=postComment.objects.filter(post=post)
            serializer = PostCommentSerializer(comments,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
