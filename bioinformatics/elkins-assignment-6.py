file = open("cftr.txt")

dnaSeq = file.readlines()[1:]  
dnaSeq = "".join(dnaSeq)
dnaSeq = dnaSeq.replace("\n", "")  
dnaSeq = dnaSeq.upper()

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

protein = ""

for r in range(0,len(dnaSeq),3):    
  s = (dnaSeq[r:r+3])  
  protein += gencode[s]   

print protein

AminoDictionary = {
   'A': 'Ala',
   'C': 'Cys',
   'H': 'His',
   'M': 'Met',
   'T': 'Thr',
   'R': 'Arg',
   'Q': 'Gln',
   'I': 'Ile',
   'F': 'Phe',
   'W': 'Trp',
   'N': 'Asn',
   'E': 'Glu',
   'L': 'Leu',
   'P': 'Pro',
   'Y': 'Tyr',
   'D': 'Asp',
   'G': 'Gly',
   'K': 'Lys',
   'S': 'Ser',
   'V': 'Val',
   '*': 'STOP'}

protein2 = ""

for r in protein:
  protein2 += AminoDictionary[r] + " "


print (protein2)

