#!/usr/bin/python


import sys
import re

p = re.compile('([^ ]*) ([^ ]*) ([^ ]*) (\[.*\]) (\".*\") ([^ ]*) ([^ ]*)')
#look at test code on lecture slides for feb 26th


for line in sys.stdin:
	data = line.strip()
	m = p.match(data)
	if not m:
		continue

	host, ignore, user, data, request, status, size = m.groups()

	#print out something here
	#prints out IP address and amount of requests
	print "{0}\t{1}".format(host,request)

	#print url and hits
	#print "{0}\t{1}".format(user,request)






