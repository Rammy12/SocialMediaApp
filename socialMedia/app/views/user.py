from rest_framework import generics
from app.serializers import UserSerializer
from app.models import User


class CreateUser(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    pass