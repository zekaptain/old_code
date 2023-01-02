import re

#FOR THURSDAY NOVEMBER 5th

my_file = open("unknown.txt")

predictions = open("predictions.txt","w")


# skip the header line in the fasta file, but string converted to list

dnaSeq = my_file.readlines()[1:]
dnaSeq = "".join(dnaSeq)

dnaSeq = dnaSeq.replace("\n", "")


#this looks for ORFs that has over 100 codons
#THIS IS THE ASSIGNMENT -- already done. part one of assignment
pattern = re.compile(r'ATG((?!TAG|TGA|TAA)...){100,}(TGA|TAG|TAA)')



#this is for amino acids
#THIS is something different -- converted a higher level pattern into regex to find amino acids. Finds pattern that binds calcium
#pattern = re.compile(r'D[^W][DNS][^ILVFYW][DENSTG][DNQGHRK][^GP][LIVMC][DENQSTAGC].{2}[DE][LIVMFYW]')


#gives number of times we find AAA in dnaSeq
hits = re.finditer(pattern,dnaSeq)

for match in hits:

	#madHitz is AAA
	madHitz = match.group()
	#starting location of AAA
	hit_start = match.start()
	#ending location of AAA
	hit_end = match.end()
	#print madHitz, hit_start, hit_end
	hit_end = hit_end + 1
	predictions.write(str(hit_start))
	predictions.write(",")
	predictions.write(str(hit_end))
	predictions.write("\n")


dnaSeq = dnaSeq.upper()

antisense = {'T':'A','A':'T','C':'G','G':'C'}

negDnaSeq = ""

for base in dnaSeq:
    negDnaSeq += antisense[base]

negDnaSeq = negDnaSeq[::-1]

hits = re.finditer(pattern,negDnaSeq)

for match in hits:

	#madHitz is AAA
	madHitz = match.group()
	#starting location of AAA
	hit_start = match.start()
	#ending location of AAA
	hit_end = match.end()
	#find the number in the ORF of the forward seq
	hit_start = len(negDnaSeq) - hit_start - 1
	hit_end = len(negDnaSeq) - hit_end
	#print madHitz, hit_start, hit_end
	predictions.write(str(hit_end))
	predictions.write(",")
	predictions.write(str(hit_start))
	predictions.write("\n")





