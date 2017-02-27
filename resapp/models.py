from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.core.validators import URLValidator
# Create your models here.

class RestaurantModel(models.Model):
    name = models.CharField(max_length = 100)
    url = models.TextField(validators = [URLValidator()])
    city = models.CharField(max_length = 20)
    address = models.CharField(max_length = 100)
    def __str__(self):
        return "{0} {1}".format(self.name,self.city)

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    restaurant = models.ManyToManyField(RestaurantModel,null = True,blank = True)
    def __str__(self):
        return "{0}".format(self.user)
