from users.models import *


import oauth2
import json
import oauth2
import optparse
import urllib
import urllib2

def crawl(area, iteCount):
    # Fill in these values
    consumer_key = '79awXH4QknbAhg9izd4lkA'
    consumer_secret = '1ko9jVKOH4QB9DsFJ4x1EsYZAmo'
    token = 'HJHR1a2Fh1xB-OTvmZkTno0NvdR6e38U'
    token_secret = '9xXxy0UEk0d0fDyLoLZByHoFwwE'

    consumer = oauth2.Consumer(consumer_key, consumer_secret)
    url = 'http://api.yelp.com/v2/search?term=restaurants&location=%s&offset=%d'%(area, 20*iteCount)

    #print 'URL: %s' % (url,)

    oauth_request = oauth2.Request('GET', url, {})
    oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                          'oauth_timestamp': oauth2.generate_timestamp(),
                          'oauth_token': token,
                          'oauth_consumer_key': consumer_key})


    token = oauth2.Token(token, token_secret)

    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)

    signed_url = oauth_request.to_url()


    print 'Signed URL: %s' % (signed_url,)


    # Connect
    try:
        conn = urllib2.urlopen(signed_url, None)
        try:
            response = json.loads(conn.read())
            for item in response['businesses']:
                yelpId = item['id']
                name = item['name']
                rating = item['rating']
                rating_img = item['rating_img_url']
                review_count = item['review_count']
                
                if('phone' in item): phone = item['phone']
                category = item['categories'][0][0]
                latitude = item['location']['coordinate']['latitude']
                longitude = item['location']['coordinate']['longitude']
                address = item['location']['address'][0]
                if('image_url' in item):
                    image = item['image_url']
                else:
                    image = None

                
                
                # Call constructor
               
                r = Restaurant(restaurantName=name, 
                            latitude=latitude, longitude=longitude,
                            category=category, averageRating=rating, 
                            yelpId=yelpId, review_count=review_count,
                            phone=phone,address=address,image=image)


                if(not Restaurant.objects.filter(yelpId = yelpId)):
                    r.save()
                    print "add Restaurant:  " + name + "  sucessfully"
                else:
                     print name + "  Skipped."
                


        finally:
          conn.close()
    except urllib2.HTTPError, error:
        response = json.loads(error.read())


def main():

    for i in xrange(8,19):
        crawl('champaign',i)