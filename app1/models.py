from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=300)
    city = models.CharField(max_length=20)
    roll = models.IntegerField()
    state = models.CharField(max_length=30)
    comment = models.CharField(max_length=100,default="No comment for this profile")


    # def __str__(self):
    #     return self.name
