from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, default='default.png', upload_to='hero_pics')
