from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist

matrix = matlist.blosum62
gap_open = -10
gap_extend = -0.5

p53_human = "MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGP"
p53_mouse = "MEESQSDISLELPLSQETFSGLWKLLPPEDILPSPHCMDDLLLPQDVEEFFEGPSEALRV"

alns = pairwise2.align.globalds(p53_human, p53_mouse, matrix, gap_open, gap_extend)

# print each of the alignments

for i in alns:
	print(i)
	
print("-----------------")

# work with the top scoring alignment

top_aln = alns[0]

# assigns each value in list to variables which can then individually be called

aln_human, aln_mouse, score, begin, end = top_aln

print (aln_human)
print (aln_mouse)
print (score)
print (end)
print (top_aln)

print (aln_human+'\n'+aln_mouse)

print("-----------------")

alns2 = pairwise2.align.localds(p53_human, p53_mouse, matrix, gap_open, gap_extend)

for i in alns2:
	print(i)

print("-----------------")

top_aln = alns2[0]
aln_human, aln_mouse, score, begin, end = top_aln

print (aln_human+'\n'+aln_mouse)
