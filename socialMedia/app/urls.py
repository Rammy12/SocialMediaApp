from django.contrib import admin
from django.urls import path
from app.views import UserResistration,UserLogin, UserProfile

urlpatterns = [
    path('register/', UserResistration.as_view(),name='register'),
    path('login/', UserLogin.as_view(),name='Login'),
    path('userProfile/', UserProfile.as_view(),name='User')
]