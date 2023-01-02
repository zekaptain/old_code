import re

#read in file
#file = open("cip1.txt","r")

#switch this to HRAS 2014 txt file
#file = open("hras2014.txt","r")

#this is for calmodulin, the amino acid regex's
#file = open("calmodulin.txt","r")

#FOR THURSDAY NOVEMBER 5th

my_file = open("unknown.txt")

# skip the header line in the fasta file, but string converted to list

dnaSeq = my_file.readlines()[1:]
dnaSeq = "".join(dnaSeq)

dnaSeq = dnaSeq.replace("\n", "")



#search for repeat AAA
#pattern = re.compile(r'AAA')

#character A repeated 3 times
#pattern = re.compile(r'[A]{3}')

#character A repeated from 3 to infinity really
#pattern = re.compile(r'[A]{3,}')

#finds either A or T in a pattern of three -gives a LOT of matches
#pattern = re.compile(r'[AT]{3}')

#search for AT in that order -- needs to be ATATAT
#pattern = re.compile(r'(AT){3}')

#look for ATG, then any three nucleotides, then either TGA, TAG, or TAA
#pattern = re.compile(r'ATG...(TGA|TAG|TAA)')

#look for a long sequence, counting by codons, ending at stop codon -- this doesn't end at stop codon
#need to take into account for triplets we DON'T want.
#pattern = re.compile(r'ATG(...)+(TGA|TAG|TAA)')

#jump out of certain regex expression if it finds a stop codon
#negative look ahead b/c says we want to exclude those of TAG, TGA, TAA pattern
#this finds all open reading frames (ORFs)
#pattern = re.compile(r'ATG((?!TAG|TGA|TAA)...)+(TGA|TAG|TAA)')

###################################################################

#this looks for ORFs that has over 100 codons
#THIS IS THE ASSIGNMENT -- already done. part one of assignment
pattern = re.compile(r'ATG((?!TAG|TGA|TAA)...){100,}(TGA|TAG|TAA)')



#this is for calmodulin
#THIS is something different -- converted a higher level pattern into regex to find amino acids. Finds pattern that binds calcium
#THIS WORKS -- part two of assignment
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
	print madHitz, hit_start, hit_end





