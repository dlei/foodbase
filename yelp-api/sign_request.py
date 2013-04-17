"""Example for signing a search request using the oauth2 library."""

import oauth2

# Fill in these values
consumer_key = '79awXH4QknbAhg9izd4lkA'
consumer_secret = '1ko9jVKOH4QB9DsFJ4x1EsYZAmo'
token = 'HJHR1a2Fh1xB-OTvmZkTno0NvdR6e38U'
token_secret = '9xXxy0UEk0d0fDyLoLZByHoFwwE'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
url = 'http://api.yelp.com/v2/search?term=restaurant&location=champaign'

print 'URL: %s' % (url,)

oauth_request = oauth2.Request('GET', url, {})
oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                      'oauth_timestamp': oauth2.generate_timestamp(),
                      'oauth_token': token,
                      'oauth_consumer_key': consumer_key})

token = oauth2.Token(token, token_secret)

oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)

signed_url = oauth_request.to_url()

print 'Signed URL: %s' % (signed_url,)
