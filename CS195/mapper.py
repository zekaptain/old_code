#!/usr/bin/python

#format of each line is:
#date\ttime\tstore name\titem description\tcost\tmethod of payment
#
#we want elements 2(store name) and 4(cost)
#We need to write them out to standard output, separated by a tab

import sys
import re

'''
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 6:
		date, time, store, item, cost, payment = data
		#print for store and cost output
		print "{0}\t{1}".format(store,cost)
		#print for item category and cost output
		#print "{0}\t{1}".format(item,cost)
'''

#code for top ten list
topTenList = []

for line in sys.stdin:

	data = line.strip().split("\t")

	if len(data) == 6:
		date, time, store, item, cost, payment = data
		topTenList.append(float(cost))
		topTenList.sort()

		if len(topTenList)>10:
			del topTenList[0]

count = len(topTenList)

for i in range (0,count):
	print topTenList[i]							
	
	
