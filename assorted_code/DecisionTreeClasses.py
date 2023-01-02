class DNode:
    """Class for an internal node of a decision tree"""
    def __init__(self,exs,attributes,possibleVals,targetColName):
        self.__availableAttributes = attributes
        self.__attribute = ''
        self.__examples = exs
        self.__colValues = possibleVals
        self.__targetCol = targetColName
        self.__childNodes = {}
        
    def chooseAttribute(self):
        self.__attribute = random.choice(self.__availableAttributes) #what a terrible way to choose the attribute!

    def train(self):
        """recursively builds the tree from the training data in __examples"""
        self.chooseAttribute() #'best' attribute at this node

        for v in self.__colValues[self.__attribute]: #going through all possible values this attribute can have
            exsForChild = self.__examples[self.__examples[self.__attribute] == v] #the subset of examples with the given value v
            
            if exsForChild.empty: #if there are no examples to pass to this child,
                                    #make a leaf with the most common among those 
                                    #at this node
                leafChild = DLeaf( self.__examples[self.__targetCol].value_counts().idxmax() )
                self.__childNodes[v] = leafChild #put the leaf in the dictionary of children nodes
                
            elif len(exsForChild[self.__targetCol].unique()) == 1: #all child examples have same class
                leafChild = DLeaf( exsForChild[self.__targetCol].unique()[0] ) #make leaf with that class
                self.__childNodes[v] = leafChild #put the leaf in the dictionary of children nodes
                
            else: #we have a regular decision node for this attribute value
                attributesForChild = list(self.__availableAttributes) #copy attributes
                attributesForChild.remove(self.__attribute) #remove the one we used at this node
                newChild = DNode(exsForChild,attributesForChild,self.__colValues,self.__targetCol)
                newChild.train() #generate the rest of the subtree for this child
                self.__childNodes[v] = newChild #put the new child node in the dictionary of children nodes
            

    def printNode(self,numIndents = 0):
        """display the tree - this isn't the prettiest representation"""
        for i in range(numIndents): print(" "), #print with no newline, this only works for Python 2
        print(self.__attribute)
        for attr in self.__childNodes.keys():
            for i in range(numIndents): print("|"),
            print(":"+attr)
            self.__childNodes[attr].printNode(numIndents+1)
                   

class DLeaf:
    """represents leaves of a decision tree"""
    def __init__(self,labelVal):
        self.__label = labelVal
    
    def printNode(self,numIndents = 0):
        for i in range(numIndents): print(" "), #print with no newline, this only works for Python 2
        print "LEAF: "+self.__label
        
        
import pandas
import random
from sklearn import cross_validation

data = pandas.read_csv('carData.csv')


#this is a disctionary we'll use to keep track of all
#possible values that any given attribute can have
possibleValuesForEachColumn  = {}

headers = ['price','maint','doors','persons','trunk','safety','acceptability']

for h in headers:
    possibleValuesForEachColumn[h] = data[h].unique()
    
#10% of the data goes into the test set, the rest into the training set   
(trainData, testData) = cross_validation.train_test_split(data,test_size = 0.1) 

#initialize the root node
t = DNode(trainData,['price','maint','doors','persons','trunk','safety'],possibleValuesForEachColumn,'acceptability')
t.train() #train the whole tree


#once you add the classify() method to the DNode and DLeaf, you can uncomment the following code
"""
numCorrect = 0.0
for i in range(len(testData)):  #go through all the testing examples
    testExample = testData.iloc[i] #current row
    prediction = t.classify(testExample) #prediction of current row
    if prediction == testExample['acceptability']: #was the prediction correct?
        numCorrect += 1.0

accuracy = numCorrect/len(testData)
print accuracy

"""

t.printNode() #print the tree to see what it looks like

