# Zeke Elkins
# 1/29/15
# intro to python lab

#import the random package
#this gives access to random.randint function
import random


print "hello"

#print list of values 0 up to 4 (not including 4)
print range(4)

#print list of values 5 up to 10 (not including 10)
print range(5, 10)

#print list of values 20 up to 40 (not including 40), counting by 2
print range(20, 40, 2)

#our first loop
for i in range(10):
	print i

#prints out string hello along with #3
print "hello", 3

#output of int variable w/i a string
val = 4
print "hello %d" %val

#while loops -- no ++ operator in python
i = 4
while i<10:
	print i
	i = i+1



#challenge #1
i = 3
while i<30:
	print i, "is a multiple of 3"
	i = i+3


#using the input function
x = input("Please enter an integer: ")
print "You entered the number", x

#this function returns a String
filename = raw_input("Enter a filename to be read: ")

#if statements
x = input("please enter an integer: ")
print "you entered the number", x

if x>3 and x<10:
	print "in range"
	print "woot woot"

elif x == 219:
	print "219!!! are you kidding me!?"

elif x>100:
	print "way too high"

else:
	print "not in the range and not too high" 

#get random number (inclusive) between 0 and 10
randomNumber = random.randint(0,10)
print randomNumber



#challenge #2
x = input("Enter the number of guesses to allow: ")
highVal = input("Enter the highest number the random number can be: ")
endGame = "false"
randomNumber = random.randint(0,highVal)

i=1
while i<x+1 and endGame == "false":

	print "Try", i
	guess = input("What is your guess: ")

	if guess > randomNumber:
		print "Your guess was too high"
	elif guess < randomNumber:
		print "Your guess was too low"

	if guess == randomNumber:
		print "You win!"
		endGame = "true"

	i = i+1

	if i == x+1 and endGame == "false":
		print "YOU LOSE. The answer was", randomNumber
		endGame = "true"



#working with text files
#open up the file called "numbers.txt" for input
#infile = open("numbers.txt", "r")
outfile = open("example.out", "w")
count = 1
outfile.write("This is the first line\n")
count = count + 1
outfile.write("This is line number %d" %count)
outfile.close()



#numbers.txt file
outfile = open("numbers.txt", "w")
outfile.write("2\n")
outfile.write("3\n")
outfile.write("4\n")
outfile.write("24\n")
outfile.close()



#opens file, reads data, outputs it
#open file called "numbers.txt" for input
infile = open("numbers.txt", "r")

#read the file contents into a string called data
data = infile.read()

#convert data to array of strings
array = data.split()

#print out the array
print array

#close the file
infile.close()



#final challenge
#print out how many even numbers there are
#in a file of string data
fileName = raw_input("enter a filename to be read: ")
infile = open(fileName, "r")
stringData = infile.read()
array = stringData.split()
infile.close()
length = len(array)
lengthNum = int(length)
#print lengthNum

infile = open(fileName, "r")
numEven = 0
i = 0
while i < lengthNum:

	
	data = infile.readline()
	numData = int(data)

	if numData %2 == 0:
		numEven = numEven + 1
	
	i = i + 1

infile.close()

print "the input file has %d even numbers" %numEven
























