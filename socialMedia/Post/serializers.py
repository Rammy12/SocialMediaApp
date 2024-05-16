from Post.models import Post
from rest_framework import serializers



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
    title=serializers.CharField()
    description=serializers.CharField()
    user=serializers.HiddenField(default=serializers.CurrentUserDefault())