import re

f = open("C:\\Users\\Wlesr\\OneDrive\\Documents\\General-Work\\AdventOfCode2020\\Day6\\Day6Input.txt", "r")

sumofCounts = 0
sumofEveryone = 0

lines = f.read()
answers = []
answers = lines.split("\n\n")
filteredlines = []




for line in answers:
    filteredlines.append(line.replace("\n",""))

def process_data(line, sumofCounts):
    set_answers = set()  
    for x in line:
        set_answers.add(x)
        
        #print(set_answers)
    sumofCounts += len(set_answers)

    #print(main_set_string)
        
    
    return sumofCounts




def set_intersection_method(group):       
    main_set = [] 
    list_test = group.splitlines()
   
    main_set = set(list_test[0])
    for set_words in range(len(list_test)):         
        main_set = main_set.intersection(list_test[set_words])      
    print(main_set)      
    return len(main_set)



for group in answers:
    sumofEveryone += set_intersection_method(group)
    

#print(answers)
print(sumofCounts)
print(sumofEveryone)

