from distutils.command import upload
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from config import settings

# Create your models here.
class Author(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    bio = models.TextField()

    def __str__(self):
        return f'{self.user.username}'

    def get_absolute_url(self):
        return reverse_lazy('author_detail', args=[str(self.id)])

    @property
    def name(self):
        return self.user.first_name + ' ' + self.user.last_name

    @property
    def articles(self):
        return Hero.objects.filter(author=self)

    @staticmethod
    def get_me(user):
        return Author.objects.get_or_create(user=user)[0]

class Hero(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, null=True)
    strength = models.CharField(max_length=200, null=True)
    weakness = models.CharField(max_length=200, null=True)
    description = models.TextField()
    #image = models.ImageField(upload_to=settings.MEDIA_ROOT, null=True)

    def __str__(self):
        return f'{self.name}'