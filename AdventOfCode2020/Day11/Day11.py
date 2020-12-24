import sys
f = open("C:\\Users\\Wlesr\\OneDrive\\Documents\\General-Work\\AdventOfCode2020\\Day11\\Day11Input.txt", 'r')

SeatAllocationArray = []
SeatLine = f.readlines()
SeatsToCheck = {}

for Specific_SeatLine in SeatLine:
    lineToAdd = Specific_SeatLine.rstrip("\n")
    SeatAllocationArray.append(list(lineToAdd))

MaxLength = len(SeatAllocationArray[0])
MaxWidth = len(SeatAllocationArray)

def FlipValue(Array):
    copyOfArray = [row[:] for row in Array]
    for row in range(len(Array)):
        for seat in range(MaxLength):
            currentRow  = row
            CurrentSeat = seat                     
            #neighbourAssignment(row, seat-1,Array)
            #neighbourAssignment(row, seat+1,Array)
            #neighbourAssignment(row-1, seat, Array)
           #neighbourAssignment(row+1,seat,Array)        
            #neighbourAssignment(row+1, seat+1,Array)        
            #neighbourAssignment(row+1, seat-1,Array)                     
            #neighbourAssignment(row-1, seat-1,Array)        
            #neighbourAssignment(row-1, seat+1,Array)  
            
            findSeat(row,seat-1, currentRow, CurrentSeat, Array)
            findSeat(row,seat+1, currentRow, CurrentSeat, Array)
            findSeat(row-1,seat, currentRow, CurrentSeat, Array)
            findSeat(row+1,seat, currentRow, CurrentSeat, Array)
            findSeat(row+1,seat+1, currentRow, CurrentSeat, Array)
            findSeat(row+1,seat-1, currentRow, CurrentSeat, Array)
            findSeat(row-1,seat-1, currentRow, CurrentSeat, Array)
            findSeat(row-1,seat+1, currentRow, CurrentSeat, Array)     
            SeatsToCheck[str([row]) + " " + str([seat])] = Array[row][seat]           
 
            if list(SeatsToCheck.values()).count("#") == 0:
                if Array[row][seat] != ".":
                    copyOfArray[row][seat] = ("#")
            elif list(SeatsToCheck.values())[:-1].count("#") > 4 and Array[row][seat] == "#":
                if Array[row][seat] != ".":
                    copyOfArray[row][seat] = ("L")         
            SeatsToCheck.clear()
    pretty_Array_print(copyOfArray)   
    return copyOfArray

def neighbourAssignment(row, seat, Array):      
    try:
        if row < 0 or seat < 0 or row > len(Array)-1 or seat > MaxLength-1:        
            return
        else: 
            SeatsToCheck[str([row]) + " " + str([seat])] = Array[row][seat]
    except:
        print("out of Bounds")

def pretty_Array_print(Array):
    print("----------------------------------")
    for row in Array:
        print(row)

def findSeat(row,seat, currentRow,CurrentSeat,Array):
    if row > currentRow:
        rowDifference = 1
    elif row < currentRow: 
        rowDifference = -1
    else:
        rowDifference = 0

    if seat > CurrentSeat:
        seatDifference = 1
    elif seat < CurrentSeat:
        seatDifference = -1
    else:
        seatDifference = 0

    seatFound = False
    while seatFound != True:
        #print(str(row) + " " + str(seat))
        try:
            if row < 0 or seat < 0 or row > MaxWidth-1 or seat > MaxLength-1:        
                return
            else: 
                if Array[row][seat] != ".":
                    seatFound = True
                    #print("Found:" + str(row) + " " +  str(seat))
                    SeatsToCheck[str([row]) + " " + str([seat])] = Array[row][seat]
        except:
            print("out of Bounds")
        row += rowDifference
        seat += seatDifference

def checkIterations():
    temp = FlipValue(SeatAllocationArray)
    orignal = []
    while temp != orignal:
        orignal = temp
        temp = FlipValue(orignal)
    OccupiedSeats = 0

    for x in orignal:
        OccupiedSeats += x.count("#")

    print(OccupiedSeats)
    
checkIterations()


