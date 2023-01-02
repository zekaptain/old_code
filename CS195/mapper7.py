#!/usr/bin/python


#Conor Wells
#Lab 8


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

p = re.compile('([^ ]*) ([^ ]*) ([^ ]*) (\[.*\]) (\".*\") ([^ ]*) ([^ ]*)')     #regular expression
#v = re.compile('([^ ]*) ([^ ]*) ([^ ]*)')

for line in sys.stdin:
	data = line.strip()
	m = p.match(data)
	if not m:
		continue
	host, ignore, user, date, request, status, size = m.groups()
	#print "{0}\t{1}".format(host,request)							#prints IP address and amount of requests
	#w = v.match(request)
	#first, second, third = w.groups()
	print "{0}\t{1}".format(host,request)
	






