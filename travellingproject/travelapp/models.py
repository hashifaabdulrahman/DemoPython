from django.db import models

# Create your models here.
class Places(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
class Team(models.Model):
    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=250)
    bio=models.TextField()