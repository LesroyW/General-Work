from itertools import combinations
import sys

f = open("Day9Input.txt", 'r')

queueOfNumbers = []
validNumber = []


lines = f.readlines()
processedlines = []

for line in lines:
    processedlines.append(int(line.rstrip()))


def checkifNumber():
    for numberToAdd in processedlines:
        if len(queueOfNumbers) == 25:
            for number in queueOfNumbers:
                if numberToAdd - number in queueOfNumbers:
                    validNumber.append(True)
            if len(validNumber) == 0:
                print(numberToAdd)
                return numberToAdd
            validNumber.clear()
            queueOfNumbers.pop(0)
            queueOfNumbers.append(numberToAdd)                    
        else:
            queueOfNumbers.append(numberToAdd)




test_number = checkifNumber()

groupOfNumbers = []
checkTotal = 0

for x in range(2, len(processedlines)):
    #print(x)
    for number in processedlines:
        
        
        if len(groupOfNumbers) == x: 
            #print(len(groupOfNumbers))
            for value in groupOfNumbers:
                checkTotal += value                
            if checkTotal == test_number:
                print(groupOfNumbers)
                groupOfNumbers.sort()   
                print(groupOfNumbers[0] + groupOfNumbers[-1]) 
                sys.exit()
            #print(str(groupOfNumbers) + " " + str(checkTotal))
            groupOfNumbers.pop(0)    
        groupOfNumbers.append(number)
      
        checkTotal = 0
    groupOfNumbers.clear()
        
    

    

#print(queueOfNumbers)