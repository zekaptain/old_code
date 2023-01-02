import math

# A "Lisp-like list" (LLL) is either None or else a pair whose first part is
# the first entry in the list and whose second part is also a Lisp-like list.

# Add an item to the start of an LLL
def insertAtStartOfLLL(lll, it):
	return (it, lll)

# Get first item in an LLL
def getFirstInLLL(lll):
	if lll==None: 
		return None
	return lll[0]

# Get all but first item in an LLL
def removeFirstFrom(lll): 
	if lll==None:
		return None
	return lll[1]

# Get last item in an LLL
def getLastInLLL(lll):
	if lll==None: 
		return None
	if lll[1]==None:
		return lll[0]
	return getLastInLLL(lll[1])

# Get all but last item in an LLL
def removeLastFromLLL(lll): 
	if lll==None:
		return None
	if lll[1]==None:
		return None
	return (lll[0], removeLastFromLLL(lll[1]))

# Add an item to the end of an LLL
def insertAtEndOfLLL(lll, it):
	if lll==None:
		return (it, None)
	return (lll[0], insertAtEndOfLLL(lll[1], it))

# Display an LLL conceptually
def LLLtoString(lll):
	return '[ ' + LLLtoString0(lll) + ']'

def LLLtoString0(lll):
	if lll==None:
		return ''
	return str(lll[0])+' '+LLLtoString0(lll[1])

# Display an LLL as it really is
def LLLtoStringFReal(lll):
	if lll==None:
		return 'None'
	return '('+str(lll[0])+','+LLLtoStringFReal(lll[1])+')'

# Sum numbers in an LLL
def sumLLL(lll): 
	if lll==None:
		return 0
	return lll[0] + sumLLL(lll[1])

# Do like map does but use an LLL instead of a Python list 
def mapLLL(fn, lll):
	if lll==None:
		return None
	return (fn(lll[0]), mapLLL(fn, lll[1]))

# Apply a list (LLL) of functions (composing them essentially) 
def applyComposedFunctions(fnlll, x):
	if fnlll==None:
		return x
	return fnlll[0](applyComposedFunctions(fnlll[1], x))

def square(x):
	return x*x

def main():

	lll = None
	for i in range(1,9):
		lll = insertAtEndOfLLL(lll, i)
	print
	print(LLLtoString(lll))
	print(LLLtoStringFReal(lll))
	print(sumLLL(lll))
	print(LLLtoString(mapLLL(square,lll)))
	print(LLLtoString(mapLLL(lambda x: x**x,lll)))
	print

	fnlll = None
	for i in range(1,9):
		fnlll = (square, fnlll)
		big = applyComposedFunctions(fnlll, 2)
		print(big)
	print

	# not originally part of the program
	fnlll = None
	for i in range(1,100):
		fnlll = (math.sin, fnlll)
		big = applyComposedFunctions(fnlll, 2)
		print(big)
	print

main()

