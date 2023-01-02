## Thursday Lab, 9/24
# working with lists
# if you have a string, type print (b[::-1]) and this will print the string backwards. WHOA

#file = open("ecoli.txt","r")
file = open("hras2014genbank.txt","r")

dnaSeq = file.read()

#print (type(dnaSeq))

origin = dnaSeq.find("ORIGIN")
#print origin #prints the index of the o in origin, an integer

#find first number after the origin (which will be 1)
startSeq = dnaSeq.find('1',origin)
#print startSeq #also prints the index 

endSeq = dnaSeq.find("//",origin)
#print endSeq

#splits string into list of strings separated by newline character 
extractedSeq = dnaSeq[startSeq:endSeq].split('\n')
#print extractedSeq[0]

sublist0 = extractedSeq[0].split() #splits the first list into lists, gets rid of white space, separated by commas
#print sublist0

#create a loop 
extractedDNA = "" #make sure this string is empty

for eachline in extractedSeq:
	sublist = eachline.split()
	extractedDNA += "".join(sublist[1:]) #get rid of first string (that numbers which line you're at) from the sublist b/c we don't want it 

#print extractedDNA #this gives continuous string of atgc's

#count num of each nucleotide
#numA = 
#numG
#numC
#numT

#next step: go back to HRAS example, can you extract out all sequence for exons? just the exons? They're shown 
#in the HRAS file. look at mRNA and see the joins section (5001 -- 5135 etc)
#after this we'll see if we can find out what the limits of the exons are instead of hardcoding it
#but that's not what we're gonna do now
#for now, extract exons within those boundaries
#from 5000 to 5135,6175 to 6339,6606 to 6785,6938 to 7098,7795 7920,8028 8309 (I already took into account starting from 0 in the list) -- 6 exons

exon1 = extractedDNA[5000:5135]
print exon1
print()

exon2 = extractedDNA[6175:6339]
print exon2
print()

exon3 = extractedDNA[6606:6785]
print exon3
print()

exon4 = extractedDNA[6938:7098]
print exon4
print()

exon5 = extractedDNA[7795:7920]
print exon5
print()

exon6 = extractedDNA[8028:8309]
print exon6



