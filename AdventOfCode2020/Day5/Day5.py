f = open("Day5Input.txt",'r')


maxpoint = 0
minPoint = 0
midpoint = 0
row = 0
column = 0
MaxValue = 0
ListofSeats = []

for letter in f:
    if letter[0] == "F":
        maxpoint = int(127 / 2)
        minPoint = 0
    else:
        minPoint = int(127 /2 + 1)
        maxpoint = 127

    for x in range(1,7):
        midpoint = (maxpoint + minPoint) / 2
        if letter[x] == "F":       
            maxpoint = int(midpoint)
        else:
            minPoint = int(midpoint)
    row = maxpoint

    if letter[7] == "R":
       maxpoint = 7
       minPoint = int(7 / 2 + 1)
  
    else:
        minPoint = 0
        maxpoint = int(7 / 2)

    for x in range(8,10):
        midpoint = (maxpoint + minPoint) / 2    
        if letter[x] == "R":
            minPoint = int((maxpoint + minPoint) - midpoint) + 1
        #print(str(minPoint) + " " + str(maxpoint))       
        else:
            maxpoint = int((maxpoint + minPoint) - midpoint) 
        #print(str(minPoint) + " " + str(maxpoint))       
         
    column = maxpoint
    
    ListofSeats.append(row * 8 + column)
    if row * 8 + column > MaxValue:
        MaxValue = row * 8 + column

#print(MaxValue)


ListofSeats.sort()

print(ListofSeats)
for x in range (0, len(ListofSeats)):
    if int(ListofSeats[x+1]) - int(ListofSeats[x]) != 1:
        print(ListofSeats[x])
