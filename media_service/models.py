from django.db import models

# Create your models here.
class MediaModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True)