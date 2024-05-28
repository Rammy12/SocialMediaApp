from django.db import models

from app.models import User
from django.utils import timezone
from datetime import timedelta


class Story(models.Model):
    content=models.FileField(upload_to='stories/')
    created_at=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def is_active(self):
        return timezone.now() < self.created_at + timedelta(hours=24)
