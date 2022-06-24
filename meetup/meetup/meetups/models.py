from django.db import models

# Create your models here.

class Users(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return  f'{self.email}--{self.password}'

    class Meta:
        verbose_name_plural = 'User Details'


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return  f'{self.name}  ({self.address})'

class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Meetup(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    # location = models.CharField(max_length=100,default='India')
    locationn = models.ForeignKey(Location, on_delete=models.CASCADE)#model.SET_NULL also can be used
    image = models.ImageField(upload_to ='images')
    participantss = models.ManyToManyField(Participant,blank=True,null=True)
    # Without null= True, if u have blank = True , for some fileds(like CharField) default empty values
    organizer_email = models.EmailField()
    date = models.DateField()

    def __str__(self):
        return f'{self.title}-{self.slug}'

