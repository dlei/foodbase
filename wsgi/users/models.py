from django.db import models
from django.contrib.auth.models import User

# Create your models here.


'''
class User(models.Model):
	#username = models.CharField(max_length=64, unique = True)
	#password = models.CharField(max_length=32)
	vegetarian = models.BooleanField(default=0)
	#email = models.CharField(max_length=64, primary_key = True)
	objects = UserManager()
'''


class FavoriteRest(models.Model):
	user = models.ForeignKey('auth.User')
	#user = models.CharField(max_length=64)
	rate = models.IntegerField(default = 0)
	restaurantName = models.CharField(max_length=128)

