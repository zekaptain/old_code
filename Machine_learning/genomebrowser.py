myFile = open("hras2014(1).txt", "r")

dnaSeq = myFile.read()

myFile.close()

origin = dnaSeq.find( 'ORIGIN' )

startSeq = dnaSeq.find ('1', origin)

endSeq = dnaSeq.find ('//', origin)

extractedSeq = dnaSeq[startSeq:endSeq].split ('\n')

extractedDNA = ""

for eachline in extractedSeq:
    sublist = eachline.split()
    extractedDNA += "".join(sublist[1:])

#print(extractedDNA)

#5001..5135,6176..6339,6607..6785,6939..7098,7796..7920,8029..8309

exons = extractedDNA[5000:5135]+extractedDNA[6175:6339]+extractedDNA[6606:6785]+extractedDNA[6938:7098]+extractedDNA[7795:7920]+extractedDNA[8028:8309]

print(exons)

