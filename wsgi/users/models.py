from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

# Create your models here.


'''
class User(models.Model):
	#username = models.CharField(max_length=64, unique = True)
	#password = models.CharField(max_length=32)
	vegetarian = models.BooleanField(default=0)
	#email = models.CharField(max_length=64, primary_key = True)
	objects = UserManager()
'''

'''
class FavoriteRest(models.Model):
	user = models.ForeignKey('auth.User')
	#user = models.CharField(max_length=64)
	rate = models.IntegerField(default = 0)
	restaurantName = models.CharField(max_length=128)
'''
    
class UserRestaurant(models.Model):
    user =models.ForeignKey('auth.User')
    restaurantId = models.IntegerField()
    rate = models.IntegerField(default = -1)
    class Meta:  
        unique_together = ('restaurantId', 'user')  
      
    primary = ('restaurantId', 'user')  



class Restaurant(models.Model):
    restaurantName = models.CharField(max_length=128)
    latitude = models.DecimalField(max_digits = 6, decimal_places = 4)
    longitude = models.DecimalField(max_digits = 6, decimal_places = 4)
    category = models.CharField(max_length=128)
    averageRating = models.DecimalField(max_digits = 2, decimal_places = 1)
    yelpId = models.CharField(max_length=128)
    review_count = models.IntegerField(default = 0)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=128)
    image = models.CharField(max_length=256)


class BMRestaurant(models.Model):
    user =models.ForeignKey('auth.User')
    restaurantId = models.IntegerField()
    class Meta:  
        unique_together = ('restaurantId', 'user')  
      
    primary = ('restaurantId', 'user')

class UserProfile(models.Model):
    user = models.ForeignKey('auth.User')
    lattitude = models.DecimalField(max_digits = 6, decimal_places = 4)
    longtitude = models.DecimalField(max_digits = 6, decimal_places = 4)

class JoinRU(models.Model):
    user = models.ForeignKey(UserRestaurant)
    restaurant = models.ForeignKey(Restaurant)

 

