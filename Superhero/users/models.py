from django.db import models
from photo.models import Image
from django.contrib.auth.models import User


class Investigator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Image, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Investigator'
