import tweepy
from textblob import TextBlob

consumer_key= 'gotBtAwotLo3zkjIWTV0CGwzk'
consumer_secret_key= 'fA0CJcyhDe3kWoClrSL88aD9nR7aPHcgfocew6xUfX7xts8MhG'

access_token= '775765231398039553-ZWz4yPhT9N99u3YqzqlnoJZXB36rs8r'
access_token_secret= 'RFqLJajEp6jjYrbAbyK429JBpyJIu8qD5ONdaoUEM4jEP'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
