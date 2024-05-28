from rest_framework import serializers
from .models import Story

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'user', 'content', 'created_at', 'is_active']
        read_only_fields = ['user', 'created_at', 'is_active']