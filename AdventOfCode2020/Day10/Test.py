from itertools import combinations


f = open('C:\\Users\\Wlesr\\OneDrive\\Documents\\General-Work\\AdventOfCode2020\\Day10\\Day10InputTest.txt', 'r')


lines = f.readlines()
processedlines = []

jolt_differences = { 1: 0, 2:0, 3:0}
Valid_Arrangement = 0


LowerValueArray = []
 

#Find where the difference is less than 3
#Have a list iterate over it and check if the sequence is vaild or not


for line in lines:
    processedlines.append(int(line.rstrip()))


processedlines.sort()
maxAdapter = int(processedlines[len(processedlines)-1]) + 3 



def processingFunction():
    for x in range(len(processedlines)):
        if x+1 != len(processedlines):
            difference = processedlines[x+1] - processedlines[x]
            if difference < 3:
                LowerValueArray.append(processedlines[x+1])
            for y in jolt_differences:
                if difference == y:
                    jolt_differences[y] += 1


def processingFunction2(set_toPass):
    set_toPass.insert(0,0)
    set_toPass.append(maxAdapter)

    ValidSet = True
    for x in range(len(set_toPass)):
        if x+1 != len(set_toPass):
            difference = set_toPass[x+1] - set_toPass[x]
            if difference > 3:
                return False
            for y in jolt_differences:
                if difference == y:
                    jolt_differences[y] += 1
    
    print(set_toPass)
    return ValidSet

Allcombos = []
processingFunction()

for x in range(len(LowerValueArray)):
    p = combinations(LowerValueArray, x)       
    Allcombos.append(list(p))


#print(processedlines)
    

temp = processedlines.copy()

for combo in Allcombos:
    for Specific_combo in combo:
        for elem in Specific_combo:
                
            temp.remove(elem)
        #print(str(temp) + " With: " + str(Specific_list_combo) + " Removed")
        validSetCombo = processingFunction2(temp) 
        temp.clear()
        temp = processedlines.copy()
                 
        if validSetCombo == True:
            Valid_Arrangement += 1
            
   
print(Valid_Arrangement)



        



#print(Allcombos)