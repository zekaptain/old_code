# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:52:10 2015

@author: zacharyelkins
"""

dnaSeq = "ACTGGTCAACGTAAACGTCGAACGTAGCAGTAGC"
print(dnaSeq)

seqLength = len(dnaSeq)
print(seqLength)

numA = dnaSeq.count("A")
numG = dnaSeq.count("G")
numC = dnaSeq.count("C")
numT = dnaSeq.count("T")
print(numA)

fractionA = numA/seqLength 
fractionA = round(fractionA,2)
print(fractionA)
print ("The fraction of A's in the sequence is", fractionA)

#what is the GC content in percentage
percentageA = 100* fractionA
print(percentageA, "%")

#melting temp calculation
melt = 64.9 + ((41 * (numG + numC - 16.4))/seqLength)

print(melt, "Celsius")



###################
myDNA = input("Sequence:")
print(myDNA)
seqLen = len(myDNA)
numA = myDNA.count("A")
numG = myDNA.count("G")
numC = myDNA.count("C")
numT = myDNA.count("T")

meltingPoint = 64.9 + ((41 * (numG + numC - 16.4))/seqLen)
print(meltingPoint)

## from this, then calculate melting point from inputted sequence

