import re

a = input("What is the start coordinate?")

a = int(a)

b = input("What is the end coordinate?")

b = int(b)

print ("Range is:", a,"to", b)


# Open sequence file

my_file = open("test-regex.txt")

# skip the header line in the fasta file, but string converted to list

dnaSequence = my_file.readlines()[1:]

# convert the list back to a string

dnaSequence = "".join(dnaSequence)

dnaSequence = dnaSequence.replace("\n", "")

# print (dnaSequence)

# remove newlines from string to make a one line sequence

d = a-1


print ("Upstream sequence:")

print (a-d)

print (dnaSequence[a-1-d:a-1])

print (a-1)

print ()

print ("Open reading frame:")

print (a)

print (dnaSequence[a-1:b])

print (b)

print()
	
print("--------------------------------------------------")
print()	

# Find minus 35 promoter site

minus35 = re.finditer(r'TT[GTC]', dnaSequence[a-d:a-1])

for match in minus35:
	hit_start = match.start()
	hit_end = match.end()
	print ("Minus 35 promoter element at:", ((a-d) + hit_start), "to", ((a-d) + hit_end-1))
	print (dnaSequence[((a-d) + hit_start):((a-d) + hit_end)])

print()
		

print ("-35 promoter site candidates")
	
print (dnaSequence[a-d:a-1])

minus35 = re.finditer(r'TT[GTC]', dnaSequence[a-d:a-1])

for match in minus35:
	hit_start = match.start()
	hit_end = match.end()
	print (" "*(hit_start-1), "^")
	
print("--------------------------------------------------")

print()


# Find minus 10 promoter site

minus10 = re.finditer(r'[TA]{3,6}', dnaSequence[a-d:a-1])

for match in minus10:
	hit_start = match.start()
	hit_end = match.end()
	print ("Minus 10 promoter element at:", ((a-d) + hit_start), "to", ((a-d) + hit_end-1))
	print (dnaSequence[((a-d) + hit_start):((a-d) + hit_end)])
	
print()



print ("-10 promoter site candidates")

print (dnaSequence[a-d:a-1])

minus10 = re.finditer(r'[TA]{3,6}', dnaSequence[a-d:a-1])

for match in minus10:
	hit_start = match.start()
	hit_end = match.end()
	print (" "*(hit_start-1), "^")

print("--------------------------------------------------")
print()	

# Find ribosome-binding sites

#rbs = re.finditer(r'(AGGA|GGAG|GAGG)', dnaSequence[a-d:a-1])

rbs = re.finditer(r'[AG]{2,6}', dnaSequence[a-d:a-1])

for match in rbs:
	hit_start = match.start()
	hit_end = match.end()
	print ("RBS at:", ((a-d) + hit_start), "to", ((a-d) + hit_end-1))
	print (dnaSequence[((a-d) + hit_start):((a-d) + hit_end)])
	
print()


print ("RBS site candidates")

print (dnaSequence[a-d:a-1])

rbs = re.finditer(r'[AG]{2,6}', dnaSequence[a-d:a-1])

for match in rbs:
	hit_start = match.start()
	hit_end = match.end()
	print (" "*(hit_start-1), "^")
	
print("--------------------------------------------------")
print()	
	
print ("lac operon promoter sequence")
print ("GCTTTACACTTTATGCTTCCGGCTCGTATGTTGTGTGG")
print ("   ^-35                   ^-10  ^rbs")





