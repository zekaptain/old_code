#opens file, reads data, outputs it
#open file called "numbers.txt" for input
infile = open("monaLisaRed.ppm", "r")

#read the file contents into a string called data
data = infile.read()

#convert data to array of strings
array = data.split()

#print out the array
print array

#close the file
infile.close()