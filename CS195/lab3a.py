#author: Zeke Elkins
#date: 2/5/15
#description: lab 3 of cloud computing

#similar to a default constructor
class Complex:
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart

x = Complex(3.0, -4.5)
print x.r, x.i

class MyClass:
	'''A simple example class'''
	i = 12345
	def f(self):
		return "hello world"

x = MyClass()

print x.f()
print MyClass.f(x)









