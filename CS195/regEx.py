#regular expression checker

import sys
import re

#p contains the regular expressions
#p = re.compile('cat')

#this p takes anything between letter k and letter d
#p = re.compile('k.*d')

#non-greedy expression
#p = re.compile('k.*?d')

#p contains the regular expressions
#a integer(at least one number), followed by a string,
#followed by a floating point number
p = re.compile('(\d.*?) (\w*) (\d.*?\.\d+)')

#FIRST VERSION
'''
while(1==1):

	str = raw_input("enter a string: ")
	m = p.match(str)  #determines if str is a match with p
	if not m:
		print str, "-- no match"

	else:
		print str, "-- MATCH"

'''

#SECOND VERSION - more like mapper.py
'''
for line in sys.stdin:   #allows you to type in lines in command prompt
	data = line.strip()  #strips the newline character 
	m = p.match(data)    #determines if a match with re

	if not m:
		print data, "-- no match"

	else:
		print data, "-- MATCH"

'''

#demonstrate the greediness of .*
'''
str = "Ever cleaned a keyboard? They're filthy!"
s = p.sub("leopard", str)  #replace elements in str to match re 
print s  #prints out "Ever cleaned a leopard? They're filthy!"

str = "Ever cleaned a keyboard? They're filthy! I'm not kidding."
s = p.sub("leopard", str)  #this demonstrates the greedy nature of .*
print s  #prints out "Ever cleaned a leoparding."
'''

#demonstrate the non-greediness of *? and +?
'''
str = "Ever cleaned a keyboard? They're filthy! I'm not kidding."
s = p.sub("leopard", str)  #replace elements in str that match re
print s  #printed out: "Ever cleaned a leopard? They're filthy! I'm not leopardding."
'''

#demonstrate the usefulness of \

str = "123 pikachu 12.1"
m = p.match(str)
myInteger, myString, myDouble = m.groups()
print myInteger
print myString  #prints out pikachu
print myDouble













