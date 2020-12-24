f = open("C:\\Users\\Wlesr\\OneDrive\\Documents\\General-Work\\AdventOfCode2020\\Day2\\Day2input.txt", 'r')

passwords = []
minAndMax = []


valid = 0
newValid = 0


for line in f:
    passwords.append(line)
    #print(line)

for password in passwords:
    password = password.split(" ")   
   
    password[0] = password[0].split("-")
    if password[2].count(password[1][0]) >= int(password[0][0]) and password[2].count(password[1][0]) <= int(password[0][1]):
        valid += 1      
    first = int(password[0][0]) - 1
    last = int(password[0][1]) - 1
    if bool(password[2][first] is password[1][0]) != bool(password[2][last] is password[1][0]):
        newValid += 1    
    print(password)            

        
print(valid)
print(newValid)    

f.close()
            
