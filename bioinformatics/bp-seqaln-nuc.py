from Bio import pairwise2

p53_human = "ACGGATGCCCGGTTTAAACCGGTTTTACGTACCGAATGCGT"
p53_mouse = "ACGGTTAAGGTTTAAACCGGTTTCCGTACCGAATGCGGCTT"

alns = pairwise2.align.globalms(p53_human, p53_mouse, 2, 0, -1, -0.5)

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

print (aln_human+'\n'+aln_mouse)

