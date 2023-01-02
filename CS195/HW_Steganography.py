#author: Zeke Elkins
#date: 2/6/15
#description: this program reads in a PPM file of the user's choice,
#"decodes" the image to find a hidden message,
#and outputs that hidden message into another PPM file
#proposed points (20 out of 20): I have completed every portion of the assignment as requested

#Mona Lisa message: map safe combo 34-16-19

#Pollock message: Eat more vegetables. Get more sleep. Drink more water.

#Whistler's message: Call your mother. She probably misses you.


#set min and max vals
minRed = 255
maxRed = 0
minBlue = 255
maxBlue = 0
minGreen = 255
maxGreen = 0
pixelOutput = "255\n"


#returns a String
fileName = raw_input("Input the name of the encoded PPM file: ")
outFileName = raw_input("Input the name of the decoded PPM file: ")


#find length of the array
infile = open(fileName, "r")

'''
stringData = infile.read()
array1 = stringData.split()
length = len(array1)
arrayLength = int(length)

'''

#read in first lines of file
line1 = infile.readline()
line2 = infile.readline()
line3 = infile.readline()
line4 = infile.readline()

#open outfile and read out first few lines
outfile = open(outFileName, "w")
outfile.write(line1)
outfile.write(line2)
outfile.write(line3)
outfile.write(line4)



pixels = True

count = 0

while pixels == True:

	#for debugging
	#print count

	nextline = infile.readline()
	
	if not nextline: break

	else:
		x = int(nextline)
		#if it's a red pixel, then
		#if count%3 == 0:

		#to find blue pixel
		if count%3 == 2:

			'''
			if x > maxRed:
				maxRed = x
			if x < minRed:
				minRed = x
			'''

			if x%2 == 0:
				outfile.write("255\n")
				pixelOutput = "255\n"

			else:
				outfile.write("0\n")
				pixelOutput = "0\n"

		#if it's a green pixel
		elif count%3 == 1:

			'''
			if x > maxGreen:
				maxGreen = x
			if x < minGreen:
				minGreen = x
			'''
			
			outfile.write(pixelOutput)

		#if it's a blue pixel
		#elif count%3 == 2:

		#if it's a red pixel
		elif count%3 == 0:

			'''
			if x > maxBlue:
				maxBlue = x
			if x < minBlue:
				minBlue = x
			'''
			
			outfile.write(pixelOutput)

	#for debugging
	#print count

	count = count + 1

'''
print "The maximum red pixel is:", maxRed
print "The minimum red pixel is:", minRed
print "The maximum green pixel is:", maxGreen
print "The minimum green pixel is:", minGreen
print "The maximum blue pixel is:", maxBlue
print "The minimum blue pixel is:", minBlue
'''

outfile.close()
infile.close()













