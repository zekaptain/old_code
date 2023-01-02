#!/usr/bin/python


#Conor Wells
#Lab 9


#Format of each line is:
#date\ttime\tstore name\ titem description\tcost\tmethod of payment
#
#We want elements 2 (store name) and 4 (cost)
#I don't know why you're reading this line, Tim, you wrote this intro.
#We need to write them out to standard output, separated by a tab
"""
import sys

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 6:
		date, time, store, item, cost, payment = data
		print "{0}\t{1}".format(store,cost)				#for initial lab code, questions 3
		#print "{0}\t{1}".format(item,cost)					#for question two to get total sales of items

		"""


import sys
import re


topTen = []

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 6:
		date, time, store, item, cost, payment = data
		topTen.append(float(cost))
		topTen.sort()
		if len(topTen)>10:
			del topTen[0]
helper = len(topTen)
for i in range (0,helper):
	print topTen[i]							
	
	