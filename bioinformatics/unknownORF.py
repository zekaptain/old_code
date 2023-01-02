import re

#open and read file

my_file = open("unknown.txt","r")
posDnaSeq = my_file.readlines()[1:]
my_file.close()

posDnaSeq = "".join(posDnaSeq)

posDnaSeq = posDnaSeq.replace("\n", "")

posDnaSeq = posDnaSeq.upper()

antisense = {'T':'A','A':'T','C':'G','G':'C'}

negDnaSeq = ""

for base in posDnaSeq:
    negDnaSeq += antisense[base]

negDnaSeq = negDnaSeq[::-1]

#genetic code

gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'}

AminoDictLong = {
	'A':'Ala',
	'C':'Cys',
	'H':'His',
	'M':'Met',
	'T':'Thr',
	'R':'Arg',
	'Q':'Gln',
	'I':'Ile',
	'F':'Phe',
	'W':'Trp',
	'N':'Asn',
	'E':'Glu',
	'L':'Leu',
	'P':'Pro',
	'Y':'Tyr',
	'D':'Asp',
	'G':'Gly',
	'K':"Lys",
	'S':'Ser',
	'V':'Val',
        '*' :'STOP'
}


AminoDictMW = {
	'A':89.0,
	'C':121.15,
	'H':155.16,
	'M':149.21,
	'T':119.12,
	'R':174.20,
	'Q':146.15,
	'I':131.17,
	'F':165.19,
	'W':204.23,
	'N':132.12,
	'E':147.13,
	'L':131.17,
	'P':115.13,
	'Y':181.19,
	'D':133.10,
	'G':75.07,
	'K':146.19,
	'S':105.09,
	'V':117.15,
        '*':0.0
}



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
	'V':4.2,
        '*':0.0
}

#find ORF

protein = ""

pattern = re.compile(r'(ATG|GTG)((?!TGA|TAG|TAA)...){100,}(TGA|TAG|TAA)')

posHits = re.finditer(pattern, posDnaSeq)

counter = 1
length = 0

for match in posHits:
    hitz = match.group()
    hit_start = match.start()
    hit_end = match.end()
    length = (hit_end - hit_start)/3 - 1
    print ("+DNA",counter, ",", hit_start+1, "-", hit_end, "length:", length)
    print()
    counter = counter + 1

    orf = posDnaSeq[hit_start:hit_end]

    print (orf[0], orf[1], orf[2])

## entered code

    a=hit_start
    b=hit_end

    d = a-100

    print ("Upstream sequence:", d, "-", a)

    print()
	
    print("--------------------------------------------------")
    print()	

    # Find minus 35 promoter site

    minus35 = re.finditer(r'TT[GTC]', posDnaSeq[d:a])

    for match in minus35:
            phit_start = match.start()
            phit_end = match.end()
            print ("Minus 35 promoter element at:", (d + phit_start), "to", (d + phit_end-1))
            print (posDnaSeq[(d + phit_start):(d + phit_end)])

    print()
	
    print("--------------------------------------------------")

    # Find minus 10 promoter site

    minus10 = re.finditer(r'[TA]{3,6}', posDnaSeq[d:a])

    for match in minus10:
            phit_start = match.start()
            phit_end = match.end()
            print ("Minus 10 promoter element at:", (d + phit_start), "to", (d + phit_end-1))
            print (posDnaSeq[(d + phit_start):(d + phit_end)])

    print()
	
    print("--------------------------------------------------")

    # Find ribosome-binding site

    rbs = re.finditer(r'[AG]{2,6}', posDnaSeq[d:a])
    
    for match in rbs:
            rhit_start = match.start()
            rhit_end = match.end()
            print ("Ribosome Binding element at:", (d + rhit_start), "to", (d + rhit_end-1))
            print (posDnaSeq[(d + rhit_start):(d + rhit_end)])

    print()
	
    print("--------------------------------------------------")

    print()

    for r in range(0,len(orf),3):
        s = orf[r:r+3]
        protein += gencode[s]
        
    print (protein)
    print ()
    protein = ""

negHits = re.finditer(pattern, negDnaSeq)

negCounter = 1

protein =""

for negMatch in negHits:
    negHitz = negMatch.group()
    negHit_start = negMatch.start()
    negHit_end = negMatch.end()
    length = (negHit_end - negHit_start)/3 - 1 
    print ("-DNA", negCounter, ",", negHit_start+1,"-", negHit_end, "length:", length)
    print()
    negCounter = negCounter +1

    orf = negDnaSeq[negHit_start:negHit_end]

    print (orf[0], orf[1], orf[2])

## entered code

    a=negHit_start
    b=negHit_end

    d = a-100

    print ("Upstream sequence:", d, "-", a)

    print()
	
    print("--------------------------------------------------")
    print()	

    # Find minus 35 promoter site

    minus35 = re.finditer(r'TT[GTC]', negDnaSeq[d:a])

    for match in minus35:
            phit_start = match.start()
            phit_end = match.end()
            print ("Minus 35 promoter element at:", (d + phit_start), "to", (d + phit_end-1))
            print (negDnaSeq[(d + phit_start):(d + phit_end)])

    print()
	
    print("--------------------------------------------------")

    # Find minus 10 promoter site

    minus10 = re.finditer(r'[TA]{3,6}', negDnaSeq[d:a])

    for match in minus10:
            phit_start = match.start()
            phit_end = match.end()
            print ("Minus 10 promoter element at:", (d + phit_start), "to", (d + phit_end-1))
            print (negDnaSeq[(d + phit_start):(d + phit_end)])

    print()
	
    print("--------------------------------------------------")

    # Find ribosome-binding site

    rbs = re.finditer(r'[AG]{2,6}', negDnaSeq[d:a])
    
    for match in rbs:
            rhit_start = match.start()
            rhit_end = match.end()
            print ("Ribosome Binding element at:", (d + rhit_start), "to", (d + rhit_end-1))
            print (negDnaSeq[(d + rhit_start):(d + rhit_end)])

    print()
	
    print("--------------------------------------------------")

    print()

    for r in range(0,len(orf),3):
        s = orf[r:r+3]
        protein += gencode[s]
        
    print (protein)
    print()
    protein = ""



