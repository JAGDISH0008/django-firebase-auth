from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(models.Model):
  firebaseid = models.CharField(max_length=100,null=True,default='')
  name = models.CharField(max_length=100)
  tenant = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
