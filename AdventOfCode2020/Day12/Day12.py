f = open('Day12Input.txt','r')




FerryInstructions = []

lines = f.readlines()

for x in lines:
    x = x.rstrip()
    instruction = []
    instruction.append(x[0])
    instruction.append(x[1:])
    FerryInstructions.append(instruction)

def processInstructions(BoatsInstructions):

    angle = 90    
    East_West = 0
    North_South = 0

    while len(BoatsInstructions) != 0:
        
        if BoatsInstructions[0][0] == "R":
            angle += int(BoatsInstructions[0][1])
        elif BoatsInstructions[0][0] == "L":
            angle -= int(BoatsInstructions[0][1])

        
        angle = angle % 360
        

        if BoatsInstructions[0][0] == "F":
            if angle == 0:
                North_South += int(BoatsInstructions[0][1])
            if angle == 180:
                North_South -= int(BoatsInstructions[0][1])
            if angle == 90:
                East_West += int(BoatsInstructions[0][1])
            if angle == 270:
                East_West -= int(BoatsInstructions[0][1])
        else:
            if BoatsInstructions[0][0] == "N":
                North_South += int(BoatsInstructions[0][1])
            elif BoatsInstructions[0][0] == "S":
                North_South -= int(BoatsInstructions[0][1])
            elif BoatsInstructions[0][0] == "E":
                East_West += int(BoatsInstructions[0][1])
            elif BoatsInstructions[0][0] == "W":
                East_West -= int(BoatsInstructions[0][1])
        


        BoatsInstructions.pop(0)
    return abs(North_South) + abs(East_West)
        

print(processInstructions(FerryInstructions))


    