from django.db import models

# Create your models here.

class Attributes(models.Model):
    
    noun = models.CharField(max_length=25)
    noun2 = models.CharField(max_length=25)
    verb = models.CharField(max_length=25)
    verb2 = models.CharField(max_length=25)
    adjective = models.CharField(max_length=25)
    adjective2 = models.CharField(max_length=25)
    item = models.CharField(max_length=25)
    place = models.CharField(max_length=25)
    animal = models.CharField(max_length=25)