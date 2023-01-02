#Zeke Elkins
#create a class that describes 
#what the day is like:
#e.g. temp, wind, day, etc


class Weather:

	'''a simple class to describe today'''

	def __init__(self, temp):
		"initialize temp to input, value to be "
		self.t = temp
		self.value = 1

	def temp(self):
		self.value = self.t


	def getValue(self):
		"accessor method; returns value"
		return self.value

	def setValue(self):
		"mutator method; sets value"
		self.value = value

