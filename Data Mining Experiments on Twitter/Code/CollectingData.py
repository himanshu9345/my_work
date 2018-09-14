import tweepy
from tweepy import OAuthHandler

consumer_key = 'Umayc6h26nLIstty28Y7nF4en'
consumer_secret = 'k9trHAqNaV4F3bLAoh0rO5wCDcsiypih0wcXdk08jjekt4mTh7'
access_token = '793873801788346368-sMGXwGzi6LMTAd5QMNXvd9hjmCKuG6o'
access_secret = 'QTd3rYvM0e558K1usiBVUjz7YtwUq8fMYJZjiL2AhXSYs'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#for status in tweepy.Cursor(api.home_timeline).items(10):
# Process a single status
# print(status.text)

#for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
#    print(status._json)