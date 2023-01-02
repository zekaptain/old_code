

file = open("rhodopsin.txt","r")
proteinSeq = file.read()

print proteinSeq 
protLen = len(proteinSeq)

AminoDictHydrophobe = {
	'A':1.8,
	'C':2.5,
	'H':-3.2,
	'M':1.9,
	'T':-0.7,
	'R':-4.5,
	'Q':-3.5,
	'I':4.5,
	'F':2.8,
	'W':-0.9,
	'N':-3.5,
	'E':-3.5,
	'L':3.8,
	'P':-1.6,
	'Y':-1.3,
	'D':-3.5,
	'G':-0.4,
	'K':-3.9,
	'S':-0.8,
	'V':4.2

}

total = 0
start = 3


#right now, prints out residues starting with very first (0) amino acid instead of starting w/ fourth amino acid (4)
for residues in proteinSeq:
	if start < (protLen - 2):
		subseq = proteinSeq[start-3:start+4] #establishes window to set bounds where we retrieve letters of seq 
		for rezidues in subseq:
			total = total + (AminoDictHydrophobe[rezidues]) #total up the hydrophobicities
		average = total/7 #have 7 residues that we added
		print(start, residues, " , ", "{:+.4f}".format(average)) #the last part formats the average to 4 decimal places
		total = 0
		start = start + 1