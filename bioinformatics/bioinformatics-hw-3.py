## hw #3
#Zeke Elkins


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

percentageA = int(percentageA)
percentageG = int(percentageG)
percentageC = int(percentageC)
percentageT = int(percentageT)

print "A",percentageA, "X" * percentageA
print "G",percentageG, "X" * percentageG
print "C",percentageC, "X" * percentageC
print "T",percentageT, "X" * percentageT


meltingPoint = 64.9 + ((41 * (numG + numC - 16.4))/seqLen)
print(meltingPoint)


numA = str(numA)
numG = str(numG)
numC = str(numC)
numT = str(numT)

newFile = open("output1.txt","a")

newFile.write("The number of A's: ")
newFile.write(numA)
newFile.write("\t")
newFile.write("X" * percentageA)
newFile.write("\n")

newFile.write("The number of C's: ")
newFile.write(numC)
newFile.write("\t")
newFile.write("X" * percentageC)
newFile.write("\n")

newFile.write("The number of T's: ")
newFile.write(numT)
newFile.write("\t")
newFile.write("X" * percentageT)
newFile.write("\n")

newFile.write("The number of G's: ")
newFile.write(numG)
newFile.write("\t")
newFile.write("X" * percentageG)
newFile.write("\n")

newFile.close()






