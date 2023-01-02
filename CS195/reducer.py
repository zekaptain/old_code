#!/usr/bin/python

import sys

salesTotal = 0
currentSale = 0
oldKey = None
highestSale = -1
#number of all sales
totalNumSales = 0
#value of all sales
totalSalesVal = 0
#number of sales from each store
storeSales = 0

#find the avg sales value from certain stores
avgSale = 0

#put each line into this declared list
findMedianList = []


#loop around the data
#it will be in the format key\tval
#where key is the store name, val is the sale amount
#
#All the sales for a particular store will be presented, 
#then the key will change and we'll be dealing with the next store

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		#something has gone wrong. skip this line.
		continue

	thisKey, thisSale = data_mapped

	if oldKey and oldKey != thisKey:
		#this is for the oldKey and current salesTotal (not highest salesTotal)
		#print"{0}\t{1}".format(oldKey, salesTotal)

		#this prints the oldKey and then avg sale of that store
		#print"{0}\t{1}".format(oldKey, avgSale)

		#this prints the oldKey and then the median sale
		print"{0}\t{1}".format(oldKey, median)

		'''
		#find highest currentSale
		print "{0}\t{1}".format(oldKey, currentSale)

		if currentSale > highestSale:
			highestSale = currentSale

		'''

		'''
		#allows us to find salesTotal of each store separately
		salesTotal = 0
		#allows us to find number of sales in each store separately
		storeSales = 0

		#allows us to restart the list for each store
		del findMedianList[:]
		'''

	oldKey = thisKey
	#helps find the value of all sales in a given store
	salesTotal += float(thisSale)
	#helps find the highest sale per store
	currentSale = float(thisSale)
	#helps find the total value of all sales
	totalSalesVal = totalSalesVal + float(thisSale)
	#helps find the total number of all sales
	totalNumSales = totalNumSales + 1

	#find the total sale from each store
	storeSales += 1

	#find avg sale
	avgSale = salesTotal/storeSales

	'''
	#add this sale to the list
	findMedianList.append(float(thisSale))
	findMedianList.sort()

	#find length of list
	count = len(findMedianList)

	#if this list is an even number, find the average of both
	#else, find the middle sale
	if count%2 == 0:
		median = (findMedianList[count/2-1] + findMedianList[count/2])/2.0
	else:
		median = findMedianList[count/2]

	'''


if oldKey != None:
	#print oldKey, "\t", salesTotal
	#print oldKey, "\t", highestSale
	#print oldKey, "\t", avgSale
	print oldKey, "\t", median 

print totalNumSales
print totalSalesVal
