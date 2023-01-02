#create a virtual die using a class 
#Zeke Elkins

from random import randrange

class MSDie:

	'''a simple example class of a multi-sided die'''

	def __init__(self, sides):
		"initialize sides to input, value to be 1"
		self.sides = sides
		self.value = 1

	def roll(self):
		"roll the die"
		self.value = randrange(1,self.sides+1)

	def getValue(self):
		"accessor method; returns value"
		return self.value

	def setValue(self, value):
		"mutator method; sets value"
		self.value = value











		