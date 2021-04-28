from django.db import models

# Create your models here.

class Blog(models.Model):
    description =  models.TextField()
    thumbnail = models.ImageField(upload_to='album/photo/')
    localtime = models.DateTimeField( auto_now_add=True)