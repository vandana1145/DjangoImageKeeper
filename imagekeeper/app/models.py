from django.db import models

# Create your models here.

class Image(models.Model):
    img = models.ImageField(upload_to="img_gallarie", verbose_name='Photo')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date & Time')
