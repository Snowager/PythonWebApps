from django.db import models
from django.contrib.auth.models import User
from photo.models import Image
from django.urls import reverse_lazy

from config import settings

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, null=True)
    strength = models.CharField(max_length=200, null=True)
    weakness = models.CharField(max_length=200, null=True)
    description = models.TextField()
    photo = models.ForeignKey(Image, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Article(models.Model):
    title = models.CharField(max_length=100, default="Article Title")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    content = models.TextField(default="Article body")
    photo = models.ForeignKey(Image, null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse_lazy('Article_list')
