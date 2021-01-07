f = open('C:\\Users\\Wlesr\\OneDrive\\Documents\\General-Work\\AdventOfCode2020\\Day13\\Day13Input.txt' , 'r')

lines = f.readlines()
timestamp = int(lines[0])
availableBuses = lines[1]
availableBuses = availableBuses.split(",")
availableBuses_offest = [element for element in availableBuses if element not in "x" ]

offsets = []

def findDifferences():
    offsetNumber = 1
    for x in range(len(availableBuses)):
        
        if availableBuses[x] == "x":
            offsetNumber += 1
        if availableBuses[x] != "x":
            offsets.append(offsetNumber)
            offsetNumber = 1
    offsets.pop(0)


def calculateDifferences(BusesID,offset):
   
   #Create a recersive function to check each modulo run
   #returns true or false if false breaks out and does and adds its own ID again
   #The check is once again done again

   matching = False
   tempNumber = int(BusesID[0])
   numberToAdd = tempNumber
  
   iteration = 0
   while matching != True:
       tempNumber += numberToAdd
       matching = numberToCheck(tempNumber,offset,BusesID)   
       iteration += 1
   print(tempNumber)

                
def numberToCheck(tempNumber,offset,BusesID):
    toReturn = True
    tempArray = BusesID[1:]
   
    for x in range(len(tempArray)):
        if (int(tempNumber) + int(offset[x])) % int(tempArray[x]) == 0:
            toReturn = True
            tempNumber += int(offset[x])       
        else:
            return False
    return toReturn

def checkForAvailabilty():
    BusID = 0
    minTime = -1
    for x in range(len(availableBuses)):
        if availableBuses[x] != "x":    
            iterNum = int(availableBuses[x])
            while iterNum < timestamp:
                iterNum += int(availableBuses[x])
            if iterNum - timestamp < minTime or minTime < 0:
                minTime = iterNum - timestamp
                BusID = int(availableBuses[x])

    return int(BusID * minTime)


print(checkForAvailabilty())
findDifferences()
print(calculateDifferences(availableBuses_offest, offsets))