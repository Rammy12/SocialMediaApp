from django.db import models

# Create your models here.
from app.models import User

class Post(models.Model):
    title=models.CharField(max_length=64)
    description=models.CharField(max_length=164)
    file = models.FileField(upload_to='uploads/')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name="posts")

    def __str__(self):
        return self.title

class PostLike(models.Model):
    post=models.ForeignKey(Post,null=False,on_delete=models.CASCADE,related_name="likes")
    user=models.ForeignKey(User,null=False,on_delete=models.CASCADE)

    class Meta:
        unique_together=(('post','user'),)
    def __str__(self):
        return self.user.username



class postComment(models.Model):
    comment_text=models.CharField(max_length=164)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,null=False,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,null=False,on_delete=models.CASCADE,related_name="comments")

    def __str__(self):
        return self.user.username