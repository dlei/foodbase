from users.models import *


def addU():

	rAll = Restaurant.objects.all()

	for r in rAll:


		m = UserRestaurant(rate=r.averageRating,
				restaurantId=r.id,
				user=User.objects.get(id=32),
				)
		m.save()