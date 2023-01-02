import re

#dna = "atgtaggcataggcttatgccttctctttattgtgaggacactgctcctacacccagccatttcatcacttggaatgcagtgagaatagctatgtttagtttgatttataagaag"
file = open("hras2014.txt","r")

dna = file.read()
#print (dna)
dna=dna.upper()
#print(dna)

if re.match('ATG', dna):
    print("ATG is found at the beginning")
else:
    print("ATG is not found at the beginning")
    
a=re.match('ATG', dna)

if re.search('ATG', dna):
    print("ATG is found in the string")
else:
    print("ATG is not found in the string")

b=re.search('ATG', dna)

print(a)
print(b)
print (type(a))
print(type(b))

print(a.group())
print(a.start())
print(a.end())

c=re.findall('ATG',dna)
print(c)
print(len(c))

hits=re.finditer(r"ATG",dna)
print(hits)

for match in hits:
    hit_start=match.start()
    hit_end=match.end()
    print("ATG", hit_start, "to", hit_end)

file = open("hw4output.txt","w")

    
