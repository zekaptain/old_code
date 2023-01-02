# Modified from General Gap Penalty, Needleman-Wunch Algorithm
# Copyleft (c) 2013. Ridlo W. Wibowo
from __future__ import print_function
# default scores and gap penalty
match = 1.
mismatch = 0.
gapPenalty = -1.
             
   
# input sequences
seq1 = raw_input("Sequence 1:")
seq2 = raw_input("Sequence 2:")

 
# print inputs, scores and gap penalty
print ("Needleman-Wunch Algorithm")
print ("Sequence 1:", seq1)
print ("Sequence 2:", seq2)
print ("Gap penalty   : ", gapPenalty)
print ("Match score   : ", match)
print ("Mismatch score: ", mismatch)
 
# initiate and calculate values of cells

lseq1 = len(seq1)
lseq2 = len(seq2)

# add extra row and column for gap values

row = lseq2+1
col = lseq1+1

# define an empty matrx

val = []

# set initial gap values
 
for i in range(row):
     val.append([i*gapPenalty]) # gap value in first column
  
for j in range(1,col):
     val[0].append(j*gapPenalty) # gap value in first row
  


# calculate values of cells by row by row, beginning from top left

for i in range(1,row):
    for j in range(1,col):
            three = []
            if (seq2[i-1] == seq1[j-1]): 
                three.append(val[i-1][j-1] + match)  # match (DL)
            else: 
                three.append(val[i-1][j-1] + mismatch) # mismatch
            three.append(val[i-1][j] + gapPenalty) # Delete--gap (L)
            three.append(val[i][j-1] + gapPenalty) # Insert--gap (U)
            val[i].append(max(three))
 
# show calculations for all cells

for i in range(row):
     for j in range(col):
        print (val[i][j], "   ", end='')
     print ()
  
# do trace back: work backward from end of sequence, beginning with lower right cell

# define empty strings for aligned sequences

sequ1 = ''
sequ2 = ''

# set indices at cell in lower left

i = lseq2
j = lseq1

# working backwards, determine left, diagonal or upper right cell that gave rise to value in current cell
# from this determination, identify whether bases are matched, mismatched, or bases is paired with a gap

while (i > 0 or j > 0):
     if (i>0 and j>0 and val[i][j] == val[i-1][j-1] + (match if seq2[i-1]==seq1[j-1] else mismatch)):  # from diagonal?
         sequ1 += seq1[j-1]
         sequ2 += seq2[i-1]
         i -= 1; j -= 1
     elif (i>0 and val[i][j] == val[i-1][j] + gapPenalty):     # from left?
         sequ1 += '-'
         sequ2 += seq2[i-1]
         i -= 1
     elif (j>0 and val[i][j] == val[i][j-1] + gapPenalty):    #from upper
         sequ1 += seq1[j-1]
         sequ2 += '-'
         j -= 1

# reverses sequences because you assembled them from their ends
  
sequ1r = ' '.join([sequ1[j] for j in range(-1, -(len(sequ1)+1), -1)])
sequ2r = ' '.join([sequ2[j] for j in range(-1, -(len(sequ2)+1), -1)])

# calculate a simple score based on number of matches or mismatches in aligned sequences
# use match = 1 and mismatch = 0 for a consisten scoring scheme (when you change values above)

matchSeq = 1
mismatchSeq = 0

score = 0

for j in range(len(sequ1)):
     if (sequ1[j] == sequ2[j]):
            score += matchSeq
     else:
            score += mismatchSeq

#add gap penalities to score
            
countGaps = sequ1r.count("-") + sequ2r.count("-")

score = score + countGaps * gapPenalty
 

# print sequence alignment
 
print ("Sequence 1: ", sequ1r)
print ("Sequence 2: ", sequ2r)
print ("Score     : ", score)
