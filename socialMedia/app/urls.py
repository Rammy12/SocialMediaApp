from django.contrib import admin
from django.urls import path
from app.serializers import UserSerializer
from app.views.user import CreateUser

urlpatterns = [
    path('/user', admin.site.urls),
]