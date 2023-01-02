# read in comma delimited coordinates file

# change inut file name to name of your file

my_file = open("genepred2.txt")

coordinateList = my_file.readlines()

coordinateList = "".join(coordinateList)

coordinateList = coordinateList.replace("\n",",")

coordinateList = coordinateList.split(",")
	
myList = [int(x) for x in coordinateList]

# write out parts of html and svg tags

head = """<!DOCTYPE html>
<html>
<body>"""

# adjust width of display here

svgBegin = """<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="11000" height="200">"""

svgEnd = "</svg>"

anyEnd = """>"""

tail = """</body>
</html>"""

recX = "<rect x=\""
recY = "\" y=\""
recR = "\" rx=\"20\" ry=\"20"
recW="\" width=\""
recH = "\" height=\""
recS= "\" style=\"fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)"
recEnd = "\"/>"

lineX1 = "<line x1=\""
lineY1 = "\" y1=\""
lineX2 = "\" x2=\""
lineY2 = "\" y2=\""
lineStyle = "\" style=\"stroke:rgb(0,0,255);stroke-width:3\""
lineEnd = "/>"

textX1 = "<text x=\""
textY1 = "\" y=\""
textStyle = "\" style= \"font-family: Arial; font-size: 14; fill : white\">"
textStyle2 = "\" style= \"font-family: Arial; font-size: 14; fill : black\">"
textEnd = "</text>"

# assign values to variables and constants

svg1 = ""

X = 0

Y = 10

height = 40

X1 = 10
X2 = int(myList[-1])
Y1 = 30
Y2 = 30

# adjust length of DNA here

lengthDNA =20807

# scaling factor between 1 and 10 (coordinates collide at >5)

scalingFactor = 2

orfNumber = 1

# write out svg for diagram

svg1 += lineX1 + str(X1) + lineY1 + str(Y1) + lineX2 + str(lengthDNA//scalingFactor)+ lineY2 + str(Y2) + lineStyle + lineEnd + "\n"

for i in range(0, len(myList), 2):
	print (myList[i], myList[i+1])
	width = int((myList[i+1] - myList[i])/scalingFactor)
	print(width)
	X = int((myList[i] + 10)/scalingFactor)
	orfTitle = "ORF" + str(orfNumber)
	midpoint = int((myList[i] + myList[i+1])/2)
	svg1 += recX + str(X) + recY + str(Y) + recR + recW + str(width) + recH + str(height) + recS + recEnd  + "\n"
	svg1 += textX1 + str((myList[i]+40)//scalingFactor) + textY1 + str(Y1+4) + textStyle + str(myList[i]) + textEnd +  "\n"
	svg1 += textX1 + str((myList[i+1]-scalingFactor*40)//scalingFactor) + textY1 + str(Y1+4) + textStyle + str(myList[i+1]) + textEnd +  "\n"
	svg1 += textX1 + str(midpoint//scalingFactor-15) + textY1 + str(Y1+40) + textStyle2 + orfTitle + textEnd +  "\n"

	orfNumber = orfNumber + 1


svg2 = head + "\n" + svgBegin + "\n" + svg1 + svgEnd + "\n" + tail
print (svg2)


# write out html and svg files

f = open('svg.html', 'w')

f.write(svg2)

svg3 = svgBegin + "\n" + svg1 + svgEnd

print(svg3)

f = open('test.svg', 'w')

f.write(svg3)








