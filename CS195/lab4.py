#lab 4
#Zeke Elkins

#this won't run if just by itself w/o the if statement
def myFunction():
	"this is an awesome function"
	print "look at me"

#name will always be main unless otherwise specified,
#so the code will call myFunction()
if __name__ == '__main__':
	myFunction()


#EXCEPTIONS

while True:
	try:
		x = int(raw_input("Please enter a number: "))
		break
	except ValueError:
		print "Oops! That was no valid number. Try again..."


#Challenge 2

while True:
	try:
		x = int(raw_input("Please enter a numerator: "))
		y = int(raw_input("Please enter a denominator: "))
		z = x/y
		print "The answer is", z
		break
	except ZeroDivisionError:
		print "Cannot divide by zero. Try again..."