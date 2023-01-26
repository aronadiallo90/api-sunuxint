from django.db import models
from PIL import Image

# Create your models here.

class Post(models.Model):
    photo = models.ImageField(null=True,verbose_name='image')
    title = models.CharField(max_length=128, verbose_name='titre')
    date_created = models.DateTimeField(auto_now_add=True)