#Printing Basic Hello world message
message = "Hello Python World!"
print(message)
#Basic Computation
result = 2 + 3;
print(result)

#Knowing that '' "" denotes a string

name = "ada lovelace"
print(name.title())
#Method title displays the string in titlecase

print(name.upper())
#Converts string name to uppercase

print(name.lower())
#converts string name to lovercase

#Combining Strings/Concatenation
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello " + full_name + "!" )

message = "Hello " + full_name + "!" #Concatenation and Assignment
print(message)

#Special Characters - Tabs and White spaces
print("\tPython")
#\t tabbed spaces

print("\nPython")
#\n new Line

white_space_removal = ' Spaces'
white_space_removal = white_space_removal.rstrip()
print(white_space_removal)
#Evaluates to 'Spaces'

#Avoiding Syntax Errors With Strings
message = "One of Python's strengths is its diverse community."
print(message)
#Use double quotes if string contains apostrophe

#Using Numbers
result = 3 ** 3
print(result)

result = 3 + 5 * 4
print(result)

result = (3+5) * 4
print(result)

#Avoid Type Errors
age = 23
message = "Happy " + str(age) + "rd Birthday!"
#message = "Happy " + age + "rd Birthday!" Causes and error as 23 is not a string
print(message)
