#textblop helps performing the sentiment analysis
from textblob import TextBlob

#tweepy is the library for accessing twitter API
import tweepy

#The following four values you can obtaing once you create application account on tweeter
consumer_key= "Z9dster0OlkbGiEGqP1wfD8Ru"
consumer_secret= "mfNJackhYPkYyFXtsx9ma40f5DqD3KTcXI5cUQZxQEc5aWVNV1"

access_token= "3345200409-yuHQCrnI1Xe76PyYs2jP2iqg7YJXWUqQUGXEKnP"
access_token_secret= "536oz4ZZT35U0PmD9AI9p5YE9Vj9y1zl0hcb4bcNUNrDW"

# authentication to login via twitter API
authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)

#setting set_access_token method on authentication
authentication.set_access_token(access_token, access_token_secret)


api_var = tweepy.API(authentication)

all_tweets = api_var.search("Putin")


#Polarity measures the sentiments whether negative or positive, and subjectivety measure how much of opinion as compared to how much factual a given text is

for tweets in all_tweets:
	print(tweets.text)
	tweet = TextBlob(tweets.text)
	total = tweet.sentiment
	print (total)
	print ("\n")


	
