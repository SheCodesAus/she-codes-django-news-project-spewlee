from http.client import MULTIPLE_CHOICES
from django.contrib.auth import get_user_model
from users.models import CustomUser
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
        )
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        related_name = "stories",
        null = True,
        blank = True
        )
    image = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

