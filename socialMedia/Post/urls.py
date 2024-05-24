from django.urls import path
from Post.views import PostView,PostDetailView,UserPostsByPkView,LikePostView,PostCommentView

urlpatterns = [
    path('post/',PostView.as_view(),name='Post'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='PostDetail'),
    path('userPost/<int:pk>/',UserPostsByPkView.as_view(),name='User post'),
    path('postlike/<int:pk>/',LikePostView.as_view(),name='Like Post'),
    path('postComment/<int:pk>/',PostCommentView.as_view(),name='Post Comment'),
]