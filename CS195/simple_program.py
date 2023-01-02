#simple program for python
#if and for and such

#if statement
x = int(raw_input("Please enter an integer: "))

if x < 0:
	x = 0
	print 'negative changed to zero'

elif x == 0:
	print 'Zero'

elif x == 1:
	print 'Single'

else:
	print 'More'


#measure some strings
words = ['cat', 'window', 'defenestrate']

for w in words:
	print w len(w)
