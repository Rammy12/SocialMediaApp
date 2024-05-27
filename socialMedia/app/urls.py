from django.contrib import admin
from django.urls import path
from app.views import UserResistration,UserLogin, UserProfile,UserChangePassword, UserFollowView,ProfileImageUploadView

urlpatterns = [
    path('register/', UserResistration.as_view(),name='register'),
    path('login/', UserLogin.as_view(),name='Login'),
    path('userProfile/', UserProfile.as_view(),name='User'),
    path('changePassword/', UserChangePassword.as_view(),name='Change Password'),
    path('follow/<int:pk>/', UserFollowView.as_view(),name='Follow'),
    path('profileImage/', ProfileImageUploadView.as_view(),name='Profile Image'),
]
