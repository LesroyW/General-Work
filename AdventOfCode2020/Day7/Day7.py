f = open("Day7InputTest.txt", 'r')

class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)
    
    
listoftrees = []
possibleBags = []
shinyTree = []
Numbers = {}
test = []



def process_data(line):
    
    test_line = line.replace(" bags contain", ",")
    test_line = test_line.replace(" bags","")
    test_line = test_line.replace(" bag","")
    test_line = test_line.replace(".\n","")

    
    
    
    test_line = list(test_line.split(","))
    #print(test_line)
    Numbers[test_line[0]] = test_line[1:len(test_line)]
    for x in range(1, len(test_line)):
        test_line[x] = test_line[x][3:]  

   
    
    return Numbers
    
for line in f:
    result = process_data(line)  
    
    #main_colour = Node(result.)
    #for x in range(1, len(result)):
        #Child_Colour = Node(result[x])
        #main_colour.add_child(Child_Colour)
    #listoftrees.append(main_colour)


#print(Numbers)

test_number = 0

def getNumber(ParenttoCheck, test_number):
    for k, value in Numbers.items():
        if k == ParenttoCheck:
            for v in value:
                amountofLuggage = v[1:2]
                if amountofLuggage.isdigit():
                    print("")                    
                    test_number += int(amountofLuggage) + int(amountofLuggage) * findChildren(v[3:])
                    
                    #print(test_number)




def findParents(childNode): 
    
    for tree in Numbers:
        
        if tree.data == childNode:                      
            for c in tree.children:                                
                print("Parent: " + tree.data + " Child: " + c.data)              
                
                shinyTree.append(c.data)
            
            
                findParents(c.data)
    #print(test)
                

def findChildren(childNode): 
    
    for tree, values in Numbers.items():
        #print(values)
        if tree == childNode:
            number_to_return = 0
            for v in values:
                number_to_return += int(v[1:2])
            

            #print(tree + " OK")
            #print(number_to_return)
           
            return number_to_return
            #for c in tree.children:                                
                #print("Parent: " + tree.data + " Child: " + c.data)              
                
                #shinyTree.append(c.data)
            
            
                #findParents(c.data)
#Need to change shiny gold to the parent name so it is recersive

getNumber("shiny gold", test_number)

def findBottomofTree(Node):
    for tree, values in Numbers.items():
        if tree == Node:
            for v in values:
                test.append(v)
                findBottomofTree(v[3:])
                
            
print(findBottomofTree("shiny gold"))

example_number = 0

for x in range(len(test)):
    if test[x] == " no other":
        test.remove(test[x])

print(test)


for x in range(len(test)):
    print(x)
    if x+1 >= len(test):
        print(example_number)
    else:
        example_number += (int(test[x][1:2]) + int(test[x][1:2])) * int(test[x+1][1:2])

#findParents("shiny gold")

#for x in shinyTree:

#print(Numbers)
#print(possibleBags[3])
#print(len(listoftrees))
#print(len(possibleBags))
#print(list(possibleBags))
#print(shinyTree)



