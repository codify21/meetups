from django.db import models

# Create your models here.

class Meetup(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    location = models.CharField(max_length=100,default='India')
    image = models.ImageField(upload_to ='images')

    def __str__(self):
        return f'{self.title}-{self.slug}'