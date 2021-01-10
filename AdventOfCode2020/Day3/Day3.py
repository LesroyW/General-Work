f = open("Day3Input.txt", 'r')

Slopes = []

for line in f:
    line = line.rstrip('\n')
    Slopes.append(line)

treesHit = 0
position = 0
level = 0

for line in Slopes:
    if level % 2 == 0:
        if position >= len(line):
            position =  0 + (position - (len(line))) 
        if line[position] == '#':
            treesHit += 1       
        position += 1  
    print(line)
    print(level)
    level += 1
   
    
f.close()

    


print(treesHit)
