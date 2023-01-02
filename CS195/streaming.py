#author: Zeke Elkins
#date: 2/17/15
#description: takes in original JSON file format and finds 
#string id of tweets in the file, the language of the tweet,
#the time at which the tweet was tweeted, and the text of the tweet
#proposed points (15 of 15): I altered the StdOutListener class in order to
#read the entire JSON format to a .txt file using the terminal command
#and then, in tweetData.py, I find the string id of the tweets, the lang 
#of the tweets, the time the tweet was tweeted, and the text of the tweet.


#wrote to file in terminal -- typed in "python streaming.py > output.txt"

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from auth import TwitterAuth
import random

class StdOutListener(StreamListener):

	#this function gets called every time a new tweet is received on the stream

	#this function, with my code, is now in JSON format when made into .txt file
	def on_data(self, data):

		'''
		j=json.loads(data)

		text=j["text"] #the text of the tweet
		print(text) #print it out

		#write to a file; ignore non ascii text
		outputFile.write(text.encode('ascii', 'ignore') + "\n")
		'''

		print data
		return True
		

	def on_error(self,status):
		print status


if __name__ == '__main__':
	try:
		#outputFile = open("output.txt", "w")

		#create the listener
		l = StdOutListener()
		auth = OAuthHandler(TwitterAuth.consumer_key, TwitterAuth.consumer_secret)
		auth.set_access_token(TwitterAuth.access_token, TwitterAuth.access_token_secret)

		#connect to the twitter stream
		stream = Stream(auth, l)

		#terms to track
		stream.filter(track=["president", "Iowa"])

		#alternately, location box for geotagged tweets
		#stream.filter(locations=[-0.530, 51.322, 0.231, 51.707]) #london
		#stream.filter(locations=[-96.0, 40.5, -91.0, 43.5]) #iowa

	except KeyboardInterrupt:
		#user pressed ctrl+c -- get ready to exit the program
		pass

	#close the file
	#outputFile.close()


	










