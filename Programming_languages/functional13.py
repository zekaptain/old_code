
import math
from types import *

# A "Lisp-like list" (LLL) is either None or else a pair whose first part is
# the first entry in the list and whose second part is also a Lisp-like list.

# Test for valid LLL structure
def isLLL(lll):
    if lll==None:
        return True
    if type(lll) is not TupleType:
        return False
    if len(lll) != 2:
        return False
    return isLLL(lll[1])

# Test if an LLL is empty
def isEmptyLLL(lll):
	return lll==None

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

# Insert an item at the start of an LLL
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

# Insert an item at the end of an LLL
def insertAtEndOfLLL(lll, it):
	if lll==None:
		return (it, None)
	return (lll[0], insertAtEndOfLLL(lll[1], it))

# Merge two LLLs to form a single LLL
def mergeLLL(lll1, lll2):
	if lll1==None:
		return lll2
	return insertAtStartOfLLL(mergeLLL(lll1[1], lll2), lll1[0])

# Reverse a list
def reverse(lll):
	if lll==None:
		return None
	return insertAtEndOfLLL(reverse(lll[1]), lll[0])

# Do like map does but use an LLL instead of a Python list 
def mapLLL(fn, lll):
	if lll==None:
		return None
	return (fn(lll[0]), mapLLL(fn, lll[1]))

# Apply (non-curried) binary op repeatedly to items in an LLL
def reduceLLL(op, lll, init):
	if lll==None:
		return init
	return op(lll[0], reduceLLL(op, lll[1], init))

# Apply (curried) binary op repeatedly to items in an LLL
def reduceCurLLL(op, lll, init):
	if lll==None:
		return init
	return op(lll[0])(reduceCurLLL(op, lll[1], init))

# Apply an LLL of functions (composing them)
def applyComposedFunctions(fnlll, x):
	if fnlll==None:
		return x
	return fnlll[0](applyComposedFunctions(fnlll[1], x))

def add(x, y):
	return x + y

def power(x, y):
	if (y < 1): return 1
	return x * power(x, y-1)

#I wrote this one
def reppow(x, y, n):
	if (n <= 0):
		return y
	return power(x,reppow(x,y,n-1))


#challenge 3
#define a function repappl (repeated application) with parameters n, f, x
#if n <= 0, return x. otherwise, return f(f(f(.....f(f(f(x))).....))). n f's here. 
def repappl(n, f, x):
	if (n <= 0):
	 return x
	return f(repappl(f,x,n-1))


#challenge 2 
currepow = lambda z : lambda x, y : reppow(x, y, z)

thrice = currepow(3) #3 takes place of z and this entire thing is function of two variables

#function addone that adds 1 to whatever you pass to it
addone = lambda x : return x + 1

#challenge 4: using lambdas, define a function crazyadd with two variables (x,y) that uses addone and repappl to compute x + y
crazyadd = lambda x, y : repappl(addone, x, y)

square = lambda x : power(x,2)

cube = lambda x : power(x,3)

powerCur = lambda x : lambda y : power(x,y)

def main():
	print
	print isLLL((1,(2,(3,(4,None)))))
	print isLLL(((1,2),(3,4)))
	print isLLL(None)
	print isEmptyLLL(None)
	print isEmptyLLL((1,(2,(3,(4,None)))))
	print
	print power(3,4)
	print square(5)
	print cube(2)
	print powerCur(3)(4)
	print powerCur(3)
	print
	lll1 = None
	for i in range(1,4):
		lll1 = insertAtEndOfLLL(lll1, i)
	lll2 = None
	for i in range(1,3):
		lll2 = insertAtEndOfLLL(lll2, -i)
	lll3 = mergeLLL(lll1, lll2)
	print LLLtoString(lll3)
	print LLLtoStringFReal(lll3)
	print LLLtoString(reverse(lll3))
	lll4 = mapLLL(square, lll3)
	print LLLtoString(lll4)
	print
	print reduceLLL(add, lll4, 0)
	lll5 = insertAtEndOfLLL(
	  insertAtEndOfLLL(
		insertAtEndOfLLL(
		  insertAtEndOfLLL(None, 
			2), 2), 2), 2)
	print LLLtoString(lll5)
	print reduceLLL(power, lll5, 1)
	print reduceCurLLL(powerCur, lll5, 1)
	fnlll = insertAtEndOfLLL(
	  insertAtEndOfLLL(
	    insertAtEndOfLLL(None, 
	      square), cube), lambda x: x+1)
	print applyComposedFunctions(fnlll, 2)

	print reppow(2,1,3)

	print crazyadd(5,7)

	print

main()
