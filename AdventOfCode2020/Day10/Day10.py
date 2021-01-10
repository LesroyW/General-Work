f = open('Day10Input.txt', 'r')

lines = f.readlines()
processedlines = []

jolt_differences = { 1: 0, 2:0, 3:0}

for line in lines:
    processedlines.append(int(line.rstrip()))

processedlines.append(0)
processedlines.sort()
maxAdapter = int(processedlines[len(processedlines)-1]) + 3 
processedlines.append(maxAdapter)


for x in range(len(processedlines)):
    if x+1 != len(processedlines):
        difference = processedlines[x+1] - processedlines[x]
        for y in jolt_differences:
            if difference == y:
                jolt_differences[y] += 1

print(jolt_differences.get(1,0) * jolt_differences.get(3,0))
