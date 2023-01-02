#### Homework 7 ####
#### Zeke Elkins ####

### ON TIME
### due to traveling to a funeral, you gave me a day extension, making this assignment turned in ON TIME

from __future__ import print_function
#problem 1
def combo(n,r):
	if n<r: 
		return 0
	if r == 0:
		return 1
	return (n * combo(n-1,r-1))/r

cur_combo = lambda r: lambda n: combo(n,r)

triangle = cur_combo(2)

def goofy(f,n):
	if n == 0:
		return 1
	return n * f(f,n-1)

addone = lambda x : x+1

def pluto(f):
	return(addone(f))

def square(x):
	return x*x

def main():

	print(combo(5,3))

	for n in range(0,6): 
		for r in range(0,6):
			print(combo(n,r),end=" ")
			#print " "
			r = r+1
		print("\n") 
		n = n+1

	for n in range(1,11):
		print(triangle(n),end=" ")
	print("\n")
	print(goofy(goofy,5))
	print(pluto(square(5)))
	print(pluto(pluto(square(5))))

main()