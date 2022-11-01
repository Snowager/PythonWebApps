from django.db import models
from django.contrib.auth.models import User


class Investigator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Investigator'
# Create your models here.
