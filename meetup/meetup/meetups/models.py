from django.db import models

# Create your models here.

class Meetup(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    location = models.CharField(max_length=100,default='India')