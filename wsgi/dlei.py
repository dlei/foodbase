from users.models import *
from random import randint


def addU():

	rAll = Restaurant.objects.all()

	for r in rAll:

		if r.id != 1 and r.id != 22 and r.id != 89:
			m = UserRestaurant(rate=int(round(r.averageRating+randint(-1,1))),
					restaurantId=r.id,
					user=User.objects.get(id=32),
					)
			m.save()


def randAdd():

	ulist = User.objects.all()
	rlist = Restaurant.objects.all()

	rlen = len(rlist)/4

	for u in ulist:
		for i in xrange(rlen):
			rid = 4*i + randint(0,3) + 1
			r = Restaurant.objects.get(id=rid)


			m = UserRestaurant(rate=int(round(r.averageRating+randint(-1,1))),
					restaurantId=r.id,
					user=User.objects.get(id=u.id),
					)
			m.save()