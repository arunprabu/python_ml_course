from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title      = models.CharField(max_length=200)
    slug       = models.SlugField(max_length=200, unique=True)
    category   = models.ForeignKey(Category, on_delete=models.CASCADE)
    author     = models.ForeignKey(User, on_delete=models.CASCADE)
    content    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published  = models.BooleanField(default=False)

    def __str__(self):
        return self.title

