# Create your models here.

from django.contrib.auth.models import AbstractUser 
from django.db import models
from django.utils import timezone

class User(AbstractUser ):
    is_ops_user = models.BooleanField(default=False)

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(default=timezone.now)