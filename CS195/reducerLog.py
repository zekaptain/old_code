#!/usr/bin/python



#Conor Wells
# Lab 8


import sys
import re

oldKey = None
highKey = None

# Loop around the data
# It will be in the format key\tval
# Where the key is to a door to an alternate dimension
#
#If you're reading this, you're probably wondering,
#why I wrote stuff in the comments. I think you should be rewarded for reading carefully

hitHigh = 0
hitCount = 0												#initializes total number of hits
#p = re.compile('([^ ]*) ([^ ]*) ([^ ]*)')
for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		#something has gone wrong. skip this line.
		continue

	thisKey,thisSale = data_mapped

	#if oldKey and oldKey != thisKey:
		#if (oldKey == "/assets/js/the-associates.js"):			#checks for the address /assets/js/the-associates.js
		#	print "{0}\t{1}".format(oldKey, hitCount)		#prints id and count of how many hits from that id
	if oldKey and oldKey != thisKey:
		#print "{0}\t{1}".format(oldKey, salesTotal)		
		#salesTotal = 0
		hitCount=0 
		#salesHigh = 0								#used for sales high

	oldKey = thisKey

	#salesTotal += float(thisSale)
	#totalSalesValue += float(thisSale)
	hitCount += 1									#counts how many hits this page has
	if hitHigh < hitCount:				#finds if the website has the highest amount of hits so far
		hitHigh = hitCount
		highKey = thisKey

if oldKey != None:
	print oldKey, "\t", hitCount

print "High hit website: ",highKey, " amount of hits:", hitHigh			#prints ID with the highest amount of hits
#print "total value of sales: ", totalSalesValue 		#prints total sales value