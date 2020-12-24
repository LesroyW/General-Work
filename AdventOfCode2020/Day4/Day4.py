import re


f = open("C:\\Users\\Wlesr\\OneDrive\\Documents\\General-Work\\AdventOfCode2020\\Day4\\test.txt" , 'r')

requirements = ["ecl:", "pid:", "eyr:" ,"hcl:", "byr:", "iyr:", "hgt:"]
valid = 0
valid_2 = 0

credentials = []
lines = f.read()
credentials = lines.split("\n\n")

for x in range(len(credentials)):
    credentials[x] = credentials[x].replace("\n", " ")
    credentials[x] = credentials[x] + " "
    
def process_line(credential_line):
    if not re.search("ecl:(amb|blu|brn|gry|grn|hzl|oth)", credential_line):              
        return False
    if not re.search("pid:[0-9]{9}\s+", credential_line):       
        return False
    if not re.search("eyr:(202\d|2030)", credential_line):                       
        return False
    if not re.search("hcl:#[0-9a-f]{6}\s+", credential_line):        
        return False
    if not re.search("byr:(19[2-9]\d|200[0-2])", credential_line): 
        return False
    if not re.search("iyr:(201\d|2020)",credential_line):        
        return False
    if not re.search("hgt:((1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in)", credential_line):
        return False
    print(credential_line)
    return True

for line in credentials:   

    #if all(x in line for x in requirements):
    #    valid += 1
       
    if process_line(line) == True:
        valid_2 += 1
        #print("\nValid: " + line) 
#test_record = "ecl:amb pid:434563474 eyr:2020 hcl:#123abf byr:1946 iyr:2020 hgt:150cm "

#print(process_line(test_record))


    

#print(valid)
print(valid_2)