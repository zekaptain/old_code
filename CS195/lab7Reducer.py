#!/usr/bin/python

import sys
import re


oldKey = None
highKey = None
requestHigh = -1
requestCount = 0
totalRequests = 0


#loop around the data
#it will be in the format key\tval
#where key is the store name, val is the sale amount
#
#All the hits for a particular user will be presented, 
#then the key will change and we'll be dealing with the next request

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		#something has gone wrong. skip this line.
		continue

	thisKey, thisRequest = data_mapped
	
	#prints out id and the number of requests by that id 
	if oldKey and oldKey != thisKey:
		#if oldKey == "10.192.56.219":
			#print "{0}\t{1}".format(oldKey,requestCount)

		print "{0}\t{1}".format(oldKey,requestCount)
		requestCount = 0


	'''		
	if oldKey and oldKey != thisKey:
		#this is for the oldKey and current salesTotal (not highest salesTotal)
		#print"{0}\t{1}".format(oldKey, salesTotal)

		#prints oldKey and current userRequest
		#print "{0}\t{1}".format(oldKey, userRequest)

		requestCount = 0
	
	'''

	totalRequests += 1

	oldKey = thisKey
	requestCount = requestCount + 1


	if requestHigh < requestCount:
		requestHigh = requestCount
		highKey = thisKey
	
	
	
print totalRequests

if oldKey != None:
	#print oldKey, "\t", salesTotal
	#print oldKey, "\t", highestSale
	print oldKey, "\t", requestCount

#print totalRequests
print highKey,requestHigh
