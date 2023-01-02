import re

my_file = open("unknown.txt","r")

#reads into array
dnaSeq = my_file.readlines()[1:]

#switches array to string
dnaSeq = "".join(dnaSeq)

#cut out new line characters
dnaSeq = dnaSeq.replace("\n","") #replaces newline with nothing

#print dnaSeq

complementDict = { 'A' : 'T', 'C' : 'G', 'G' : 'C', 'T' : 'A'}

compSeq = ""

#flips the DNA to its complement
for base in dnaSeq:
	compSeq += complementDict[base]

#print compSeq

#reverse DNA sequence
revdnaSeq = compSeq[::-1]

#print revdnaSeq

#find ORFs on dnaSeq and revdnaSeq
pattern = re.compile(r'ATG((?!TAG|TGA|TAA)...){100,}(TGA|TAG|TAA)')

forward = re.finditer(pattern,dnaSeq)

counter = 1
for match in forward:

	#madHitz is AAA
	madHitz = match.group()
	#starting location of AAA
	hit_start = match.start()
	#ending location of AAA
	hit_end = match.end()

	#length of ORF
	orfLength = len(madHitz) / 3

	print madHitz, hit_start, hit_end
	print orfLength
	print counter
	counter += 1

print "#############"
backward = re.finditer(pattern,revdnaSeq)

counter = 1
for match in backward:

	#madHitz is start codon
	madHitz = match.group()
	#starting location of start codon
	hit_start = match.start()
	#ending location of end codon/ORF
	hit_end = match.end()

	#length of ORF
	orfLength = len(madHitz) / 3

	print madHitz, hit_start, hit_end
	print orfLength
	print counter
	counter += 1



