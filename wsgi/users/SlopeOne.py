class SlopeOne(object):
	def __init__(self):
		self.diffs = {}
		self.freqs = {}



	def update(self, data):
		favList = list(UserRestaurant.objects.all())

		for item in favList:
			self.freqs.setdefault(rid, {})
			self.diffs.setdefault(rid,{})
			for item2 in favList:
				self.freqs[item].setdefault(item2, 0)
				self.diffs[item].setdefault(item2, 0.0)
				self.freqs[item][item2] += 1
				self.diffs[item][item2] += item.rate - item2.rate
		for item
				