#--------------------------------------------------------------------------------------------------------------------------#
#Reading an Entire file
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
#Path file looks in current directory if we want it to look somewhere else have to specific path
#Can use backslash on window systems to look for file
#Some_folder/some_file.txt - relative file path
#C:/Users..ect - absolute file path
#best to store absolute file paths as variables and pass those through
#--------------------------------------------------------------------------------------------------------------------------#
#Using loops to examine each line within a file
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
#--------------------------------------------------------------------------------------------------------------------------#
#Making a list from lines from a file
filename = 'pi_digits.txt'
listFromFile = []
#One way of reading lines from a file and adding it to a list
with open(filename) as file_object:
    for line in file_object:
        listFromFile.append(line.rstrip())
    print(listFromFile)
#Another way of reading lines
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

print(lines)
pi_string = ""
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

#--------------------------------------------------------------------------------------------------------------------------#
#Dealing with Larger files:
filename = 'pi_more_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line
print(pi_string[:52] + "...")

birthday = input("What is the date of you birthday in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday is in the Pi string")
else:
    print("Your birthday is not in the Pi string")
#--------------------------------------------------------------------------------------------------------------------------#
#Writing to an empty file
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("Hello world!")

with open(filename, 'w') as file_object:
    file_object.write("Hello. ")
    file_object.write("World.")

with open(filename, "a") as file_object:
    file_object.write("1st step.\n")
    file_object.write("2nd step.")
#--------------------------------------------------------------------------------------------------------------------------#
#Handling ZeroDivisionError
#Python throws error when trying to divide by 0
#e.g print(5/0)
#To resolve this use try/except blocks

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
#Page 201

print("Give me two numbers, and I'll divide them")
print("Enter 'q' to quit")

first_number = input("\n The first number is: ")
if first_number == 'q':
    first_number = 0
second_number = input("\n The second number is: ")
    #use of exception
try:
    answer = int(first_number)/int(second_number)
except ZeroDivisionError:
    print("This is not a valid calculation")
else:
    print(answer)
#--------------------------------------------------------------------------------------------------------------------------#
#File exceptions
filename = "Alice.txt"
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = filename + " cannot be found please try again!"
    print(msg)
#--------------------------------------------------------------------------------------------------------------------------#
#Analysing text
title = "AliceInWonderland.txt"

def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
            msg = filename + " cannot be found please try again!"
            print(msg)
    else:
        words = contents.split()
        print("This file contains " + str(len(words)) + " within it.")

list = [title, "ThreeMusketers.txt", 'MissingFile.txt']
for name in list:
    count_words(name)
#--------------------------------------------------------------------------------------------------------------------------#
