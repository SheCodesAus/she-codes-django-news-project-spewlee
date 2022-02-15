from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField, ImageField, URLField

# Create your models here.
class CustomUser (AbstractUser):
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    profile_pic = models.URLField(blank=True, null=True)
    bio = models.TextField(max_length=2000, blank=True, null=True)
    
    def __str__(self):
        return self.username