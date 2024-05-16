from django.contrib import admin
from django.urls import path,include
from Post.views import PostView,PostDetailView,UserPostsByPkView,LikePostView

urlpatterns = [
    path('post/',PostView.as_view(),name='Post'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='PostDetail'),
    path('usrePost/<int:pk>/',UserPostsByPkView.as_view(),name='User post'),
    path('postlike/<int:pk>/',LikePostView.as_view(),name='Like Post'),
]