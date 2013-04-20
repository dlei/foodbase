
from copy import *
from models import *

class SlopeOne(object):
    def __init__(self):
        self.diffs = {}
        self.freqs = {}

    def predict(self, userprefs):
        preds, freqs = {}, {}
        for item, rating in userprefs.iteritems():
            for diffitem, diffratings in self.diffs.iteritems():
                try:
                    freq = self.freqs[diffitem][item]
                except KeyError:
                    continue
                preds.setdefault(diffitem, 0.0)
                freqs.setdefault(diffitem, 0)
                preds[diffitem] += freq * (diffratings[item] + rating)
                freqs[diffitem] += freq
        return dict([(item, value / freqs[item])
                     for item, value in preds.iteritems()
                     if item not in userprefs and freqs[item] > 0])

    def update(self, userdata):
        for ratings in userdata.itervalues():
            for item1, rating1 in ratings.iteritems():
                self.freqs.setdefault(item1, {})
                self.diffs.setdefault(item1, {})
                for item2, rating2 in ratings.iteritems():
                    self.freqs[item1].setdefault(item2, 0)
                    self.diffs[item1].setdefault(item2, 0.0)
                    self.freqs[item1][item2] += 1
                    self.diffs[item1][item2] += rating1 - rating2
        for item1, ratings in self.diffs.iteritems():
            for item2 in ratings:
                ratings[item2] /= self.freqs[item1][item2]
'''
if __name__ == '__main__':
    userdata = dict(
        alice=dict(squid=1.0,
                   cuttlefish=0.5,
                   octopus=0.2),
        bob=dict(squid=1.0,
                 octopus=0.5,
                 nautilus=0.2),
        carole=dict(squid=0.2,
                    octopus=1.0,
                    cuttlefish=0.4,
                    nautilus=0.4),
        dave=dict(cuttlefish=0.9,
                  octopus=0.4,
                  nautilus=0.5),
        )
    s = SlopeOne()
    s.update(userdata)
    print s.predict(dict(squid=0.4))
'''





def init():
    users = UserRestaurant.objects.all().values('user').annotate(user_count=Count('user'))
    globalDict=dict()
    for user in users:
        userObj = User.objects.get(id=user['user'])
        user_dict=dict()
        for r in UserRestaurant.objects.filter(user=userObj):
            user_dict[r.restaurantId] = r.rate


        globalDict[user['user']] = deepcopy(user_dict)
        

    s=SlopeOne()
    s.update(globalDict)
    return s


def result(uid):
    users = UserRestaurant.objects.all().values('user').annotate(user_count=Count('user'))
    globalDict=dict()
    for user in users:
        userObj = User.objects.get(id=user['user'])
        user_dict=dict()
        for r in UserRestaurant.objects.filter(user=userObj):
            user_dict[r.restaurantId] = r.rate


        globalDict[user['user']] = deepcopy(user_dict)
    print globalDict    

    s=SlopeOne()
    s.update(globalDict)


    userObj = User.objects.get(id=uid)
    u=dict()


    for r in UserRestaurant.objects.filter(user=userObj):
            u[int(r.restaurantId)] = int(r.rate)
    #print u
    #u={8: 5, 9:2, 7:4, 52:2, 67:3}
    #u = {8: 3, 9: 3, 52: 4, 7: 5, 98:2}


    print s.predict(u)

    return s.predict(u)






