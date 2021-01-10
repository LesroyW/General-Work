import sys

f = open("Day8Input.txt" , "r")

lines = []

accumulator = 0
lineValue = 0
linesVisted = set()
listofNop_Jmp = []
orginalInst = ""
currentEntryNumber = 0




for line in f:
    lines.append(line.split(" "))




def instructionProcessor(lineValue, accumulator): 
    
    if lineValue < len(lines):
    

        if lineValue in linesVisted:        
            print("LINE DUPLICATE: " + str(lines[lineValue]) + " " + str(lineValue) + " ACC: " + str(accumulator)) 
            linesVisted.clear()
            accumulator = 0      
            return 0  
        else:        
            linesVisted.add(lineValue)    
            if lines[lineValue][0] == "acc":
                if lines[lineValue][1][0] == "+":
                    accumulator += int(lines[lineValue][1][1:])
                    lineValue += 1                
                else:
                    accumulator -= int(lines[lineValue][1][1:])
                    lineValue += 1               
    
            if lines[lineValue][0] == "jmp":
                listofNop_Jmp.append(lines[lineValue])
                if lines[lineValue][1][0] == "+":
                    lineValue += int(lines[lineValue][1][1:])    
                else:
                    lineValue -= int(lines[lineValue][1][1:])
                   
            if lineValue < len(lines):
                if lines[lineValue][0] == "nop":
                    listofNop_Jmp.append(lines[lineValue])
                    lineValue += 1
        
            instructionProcessor(lineValue, accumulator)
    else:
        print("Finished: " + int(accumulator))

def changeInstruction(entryToChange):
    if listofNop_Jmp[entryToChange][0] == "nop":        
        listofNop_Jmp[entryToChange][0] = "jmp"
    else:
        listofNop_Jmp[entryToChange][0] = "nop"
    instructionProcessor(0,accumulator)

def revertInstruction(entryToRevert):
    if listofNop_Jmp[entryToRevert][0] == "jmp":        
        listofNop_Jmp[entryToRevert][0] = "nop"
    else:
        listofNop_Jmp[entryToRevert][0] = "jmp"

def CheckChanged():
    for x in range(len(listofNop_Jmp)):
        print(str(listofNop_Jmp[x]) + "- Instruction to change")
        changeInstruction(x)
        revertInstruction(x)
        

    
instructionProcessor(0, accumulator)
CheckChanged()

