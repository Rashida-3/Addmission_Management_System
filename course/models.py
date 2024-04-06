from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission
from .manager import CustomBaseUserManager


# Create your models here.

class USerMaster(models.Model):
     CHOICES = (
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('FullStack', 'FullStack'),
    )
     name=models.CharField(max_length=200)
     email=models.EmailField()
     phone=models.CharField(max_length=10)
     date_of_birth=models.DateTimeField()
     city=models.CharField(max_length=100)
     my_field = models.CharField(max_length=50, choices=CHOICES)
     created_at=models.DateTimeField(auto_now_add=True)
     updated_at=models.DateTimeField(auto_now_add=True)
     is_active=models.BooleanField(default=True)
    #  is_staff=models.BooleanField(default=True)
    #  is_superuser=models.BooleanField(default=True)

     objects = CustomBaseUserManager()

     USERNAME_FIELD='name'
     REQUIRED_FIELDS=[]      

     def __str__(self):
        return self.name
     
     
