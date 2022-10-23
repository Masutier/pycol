from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_add']

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comm = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_add']
