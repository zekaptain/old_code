from __future__ import print_function
a = "actgggaccttgagagatttcaaccgt"
b = "atttgggggttacatactagtagtact"

len1 = len(a)
len2 = len(b)

match = 0
mismatch = 0

'''
#zip compares items in a to items in b
for i,j in zip(a,b):
	if i==j:
		print "match",i,j
		match = match +1
	else:
		print "mismatch",i,j
		mismatch = mismatch + 1

print match
print mismatch
print float(match)/float(len(a))*100, "%","similarity"
'''

#########################

#prints out both dnaSeqs and puts a bar in between the ones that are the same
'''

mismatches = []

for position in range(0,min(len1,len2)):
	if a[position] != b[position]:
		mismatches.append(" ")
	else:
		mismatches.append("|")

print a
str1 = ''.join(mismatches)
print str1
print b
'''

########################

#dot plot program

print ("  ",end="") #avoids generating a newline

for i in range(len1):
	print (a[i], "", end="")

print()

for j in range(len2): #length of b string
	print (b[j], "", end="")
	for k in range(len2): #for length of b string 
		if b[k] == a[j]:
			print (". ", end="")
		else:
			print ("  ",end="")
	print ()





