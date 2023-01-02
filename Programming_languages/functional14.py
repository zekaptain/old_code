
# Compute x^y (x raised to the y)
def power(x, y):
	if (y <= 0): return 1
	return x * power(x, y-1)

# Compute x^(x^(...(x^y)...)) with n x's 
def reppow(x, y, n):
	if (n <= 0): return y
	return power(x, reppow(x, y, n-1))

# Produces a x^(x^(...(x^y)...)) function with prescribed number of x's
curreppow = lambda n : lambda x, y : reppow(x, y, n)

# thrice is now the function x^(x^(x^y)))
thrice = curreppow(3)

# Compute f(f(...(f(x))...)) using n f's
def repappl(f, x, n):
	if (n <= 0): return x
	return f(repappl(f, x, n-1))

addone = lambda x : x+1 

# Compute (...((x+1)+1)...)+1 using y "plus ones"
crazyadd = lambda x, y : repappl(addone, x, y)
 
def main():
	print (reppow(2,1,3))         # print 2^(2^(2^1))
	print (reppow(5,4,2))         # print 5^(5^4)
	print (thrice(2,2))           # print 2^(2^(2^2))
	print (thrice(2,3))           # print 2^(2^(2^3))
	print (repappl(addone, 5, 7)) # print 5+7
	print (crazyadd(5, 7))        # print 5+7

main()
