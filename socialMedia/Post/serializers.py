from Post.models import Post,postComment,PostLike
from rest_framework import serializers



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
    title=serializers.CharField()
    description=serializers.CharField()
    user=serializers.HiddenField(default=serializers.CurrentUserDefault())


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=postComment
        fields='__all__'
    comment_text=serializers.CharField(max_length=164)
    user=serializers.HiddenField(default=serializers.CurrentUserDefault())
    post=serializers.PrimaryKeyRelatedField(read_only=True)
    def save(self, **kwargs):
        self.post=kwargs['post']
        return super().save(**kwargs)
    
class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostLike
        fields='__all__'
    user=serializers.PrimaryKeyRelatedField(read_only=True)
    post=serializers.PrimaryKeyRelatedField(read_only=True)
