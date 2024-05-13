from django.contrib import admin
from django.urls import path
from app.views import UserResistration,UserLogin

urlpatterns = [
    path('register/', UserResistration.as_view(),name='register'),
    path('login/', UserLogin.as_view(),name='Login'),
]