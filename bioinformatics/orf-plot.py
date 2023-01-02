from graphics import *

my_file = open("gene-predictions.txt")

coordinateList = my_file.readlines()

coordinateList = "".join(coordinateList)


coordinateList = coordinateList.replace("\n",",")


coordinateList = coordinateList.split(",")
	

myList = [int(x) for x in coordinateList]

#Scaling factor

x=25

end = int(myList[-1])

end = end/x

print("Scaled sequence is", end, "pixels wide.")

win = GraphWin('title',900,1500)

shape0 = Line(Point(0,15), Point(end, 15))
shape0.setArrow("last")
shape0.draw(win)


y=25

for i in range(0, len(myList), 2):
	
	print (myList[i], myList[i+1])
	shape1 = Rectangle(Point(myList[i]/x,y), Point((myList[i+1])/x,y+30))
	shape1.setOutline("black")
	shape1.setFill("yellow")
	shape1.draw(win)
	y=y+30
	
p = win.getMouse()