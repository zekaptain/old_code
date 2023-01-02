## hw #2
from __future__ import division
myFile = open("hras2014.txt", "r")

a = type(myFile)
#print a

dnaSeq = myFile.readlines()
b = type(dnaSeq)
#print b
#print dnaSeq
myFile.close()

dnaSeq1 = "".join(dnaSeq)
c = type(dnaSeq1)
#print c
#print dnaSeq1
seqLen = len(dnaSeq1)

numA = dnaSeq1.count("A")
numG = dnaSeq1.count("G")
numC = dnaSeq1.count("C")
numT = dnaSeq1.count("T")

print numA
print seqLen
print numA / seqLen


percentageA = numA / seqLen * 100
percentageG = (numG / seqLen * 100)
percentageC = (numC / seqLen * 100)
percentageT = (numT / seqLen * 100)

int(percentageA)

print "A",percentageA, "X" * percentageA
print "G",percentageG
print "C",percentageC
print "T",percentageT


meltingPoint = 64.9 + ((41 * (numG + numC - 16.4))/seqLen)
print(meltingPoint)

newFile = open("output1.txt","a")