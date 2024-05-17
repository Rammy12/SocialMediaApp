from django.db import models

# Create your models here.
from app.models import User

class Post(models.Model):
    title=models.CharField(max_length=64)
    description=models.CharField(max_length=164)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class PostLike(models.Model):
    post=models.ForeignKey(Post,null=False,on_delete=models.CASCADE)
    user=models.ForeignKey(User,null=False,on_delete=models.CASCADE)

    class Meta:
        unique_together=(('post','user'),)



class postComment(models.Model):
    comment_text=models.CharField(max_length=164)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,null=False,on_delete=models.CASCADE)

