#-------- Family Tree Solution --------#

Developed using Python3.

→  Files Content..

familyTree.py

It contains  class familyTreeNode : 

Attributes : 

name    →  name of the node connected to the tree 
gender    →  gender of the connected node
partnerName   →  name of partner (husband or wife if  any else None) node
partnerGender    →  gender of partner (husband or wife if  any else None) node
parent    →  Object of same class which points to its parents node
children    →  list of child nodes connected to it. 

Methods :

Initializes node attributes for the tree
__init__(self, name , gender , partnerName = None , partnerGender = None)
 
Adds child to the family tree  
addChildNode (self , child)


Every getRelationship**** method returns a list of their respective relatives.
e.g. : getRelationSon( ) : it returns the child of the current node with gender “Male”
         getRelationSiblings( ) :  it returns every child of the current’s →  parent node.
getRelationship****(self)

Can be used to print the family tree from the current node
printFamilyTree(self)




usableFunction.py

It contains  class usableFunctions :
from familyTree.py imports familyTreeNode

Methods :

Generates the family tree  by initializing familyTreeNode and addChildNode to its parents
makeFamilyTree(self)


SearchMember*** is used to find the node with the name passed in arguments. It calls itself recursively to find the node in the whole familyTree.
e.g : 
 searchMemberInTheTreeGet ( --- )    →  searches all  the nodes and returns  a node with name passed in arg.
searchMemberInTheTree ( --- )   →  searches only for  the node with partner and returns  a node with name passed in arg.
searchMemberInTheTreeGet( self, familyHead , name )
searchMemberInTheTree( self, familyHead , name  )


##-------------------------------------------------------------------------------------------------## 
Below Methods are Used In main.py file to process the input and do the task according to it.
##-------------------------------------------------------------------------------------------------##

It calls the method    →    searchMemberInTheTree ( --- )   →   uses the node returned by it, and adds the child to the received node in the tree.
addInputChild( self, familyHead , motherName , childName , childGender )


It calls the method    →  searchMemberInTheTreeGet ( --- )   →   uses the node returned by it, and finds the relation in the argument of the received node.
getRelationshipOfMember(self, familyHead , name , relation )



main.py

It contains  main( )  method  for actual execution :
from familyTree.py imports familyTreeNode
from usableFunction.py imports usableFunctions

→ Using object of usableFunctions and its methods, initial tree is generated.
→ Reads input from external file line by line.
→ For each line performs suitable actions by calling :
                 addInputChild and getRelationshipOfMember



How to execute the file :  Run the following command  :

python -m geektrust “path_of_input_file”

eg : python -m geektrust “C:\Users\familyTreeSolution\input.txt”




NOTE :

mainfile1.py  
This is a single file contains all the functionalities to be performed. It takes input from input file.

How to execute the file :  Run the following command  :
python -m mainfile1 “path_of_input_file”
eg : python -m mainfile1 “C:\Users\familyTreeSolution\input.txt”

mainfile2.py 
This is a single file contains all the functionalities to be performed. It takes input manually 

How to execute the file :->  Run the following command  :
python  mainfile2.py 
