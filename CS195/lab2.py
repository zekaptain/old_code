#author: Zeke Elkins
#description: lab 2



#lists
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1,2,3,4,5]
list3 = ["a", "b", "c"]

print list1

groceryList = ["apples", "bananas", "cabages", "dates"]
print groceryList[2]

#indices can also be negative,
#which means it counts from the right of the list
print "index at -1 is:", groceryList[-1]
print "index at -2 is:", groceryList[-2]

#slicing lists

#create a list of ints b/w 0 and 9
numbers = range(10)
print numbers

#now get a "slice" of the list
numberSlice = numbers[3:5]
print numberSlice

#not putting a second number will give a slice to the end
numberSlice2 = numbers[5:]
print numberSlice2



#challenge #1
numberRange = range(100)
numSlice = numberRange[50:60]
print numSlice
numSlice2 = numberRange[80:]
print numSlice2


#appending and deleting lists
groceryList = ['apples', 'bananas', 'cabbages', 'dates']
#oh, don't forget the eggs
groceryList.append('eggs')
print groceryList
#delete the bananas
del groceryList[1]
print groceryList
#remove function removes first item on the list
#delete the dates
groceryList.remove('dates')
print groceryList 

#also easy to loop through values on a list
someNumbers = [1,2,4,8]
for x in someNumbers:
	print x



#FUNCTIONS

#general layout

def functionname ( parameters ):
	"function_docstring"
	function code goes here
	return [expression] #this is optional

#example
def printme( str ):
	"this prints a string passed into this funciton"
	print str

#call the function
printme("hello")

#passing by reference
def changeme( mylist ):
	"this changes a passed list into this function"
	mylist.append([1,2,3,4])
	return

alist = [10,20,30]
print "list BEFORE the function call", alist
changeme(alist)
print "list AFTER the function call", alist

#returning a value
def addOne( x ):
	"This function adds one to the input param and returns it"
	x=x+1
	return x
print addOne(11)

#CHALLENGE 2
def addOneToList( myList ):
	#don't loop through elements
	#loop through index
	for i in range(0, len(myList)):
		myList[i] = myList[i] + 1  
	
	return myList 

evens = range(0,10,2)
print "Here are some even nums:", evens
odds = addOneToList(evens)
print "Here are some odd nums:", odds









