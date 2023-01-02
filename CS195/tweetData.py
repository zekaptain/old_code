#author: Zeke Elkins
#date: 2/17/15
#description: takes in original JSON file format and finds 
#string id of tweets in the file, the language of the tweet,
#the time at which the tweet was tweeted, and the text of the tweet

import json
import random

#print out user data
tweets = []
inputFile = open("output.txt", "r")
for line in inputFile:
	try:
		tweet = json.loads(line)
		tweets.append(tweet)
	except:
		pass

#length of array
length = len(tweets)
print length
randomNum = random.randint(0,length) 
print randomNum
tweet = tweets[randomNum]

'''
#print the ids of every tweet in the file
ids = [tweet['id_str'] for tweet in tweets]
print ids
#prints every text of every tweet in the file
texts = [tweet['text'] for tweet in tweets]
print texts
#prints every time that tweet was tweeted in the file
times = [tweet['created_at'] for tweet in tweets]
print times
'''

#prints id in string format of random tweet
print tweet['id_str']

#prints language in which tweet was written
print tweet['lang']

#prints time that tweet was created
print tweet['created_at']

#prints text of random tweet
print tweet['text']



