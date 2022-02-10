from unicodedata import category
from django.contrib.auth import get_user_model
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
        )
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    category = models.CharField(max_length=200, default='General')
    image = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title