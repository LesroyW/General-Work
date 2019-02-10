#--------------------------------------------------------------------------------------------------------------------------#
#Basic user input
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#Input prompt should be clear and easy
name = input("Please enter your name: ")
print("Hello " + name + "!")
#--------------------------------------------------------------------------------------------------------------------------#
prompt = "We are first going to learn your name."
prompt += "\nWhat is your name: "
name = input(prompt)
print("Hello " + name + "!")
#--------------------------------------------------------------------------------------------------------------------------#
#All inputs are interpreted as a string.
prompt = "What is your age? "
age = input(prompt)
print( int(age) >= 20) #Fixes the int input to string problem
#--------------------------------------------------------------------------------------------------------------------------#
#Using user input in if Statements
prompt = "How old are you? "
age = input(prompt)
if int(age) > 20:
    print("You can purchase the alcohol.")
else:
    print("You cannot purchase alcohol.")
#--------------------------------------------------------------------------------------------------------------------------#
#Modulo Operator
prompt = "I can tell you a number is even or odd: "
number = input(prompt)
if int(number) % 2 == 0:
    print(str(number) + " is even")
else:
    print(str(number) + " is odd")
#--------------------------------------------------------------------------------------------------------------------------#
#WHILE LOOPS

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "Tell me something, and I will repeat it back to you: "
prompt += "\nUntil you quit. "

command = ""

while command != "Quit":
    command = input(prompt)
    if command != "Quit":
        print(command)

prompt = "Tell me something, and I will repeat it back to you: "
prompt += "\nUntil you quit. "
test = ""
#Addition of a flag
active = True
while active:
    test = input(prompt)
    if test == "Quit":
        active = False
    else:
        print(test)
#Using a break within the while Loop
prompt = "Tell me something, about yourself: "
prompt += "\nUntil you say 'quit'. "
detail = ""

active = True
while active:
    detail = input(prompt)
    if detail == "Quit":
        break
    else:
        print(detail)

#Using a continue within the while loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
#--------------------------------------------------------------------------------------------------------------------------#
#Using Lists and Dicitionaries
unconfirmed_users = [ 'Jerry', 'Lee', 'Mack']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(current_user.title() + " is being verified. Success")
    confirmed_users.append(current_user)

for user in confirmed_users:
    print(user)

#Removing instances of specific value
numbers = [1,4,56,23,5,2,1,5,7,23,2,5,7,3,6]
while 5 in numbers:
    numbers.remove(5)
print(numbers)

#Filling a dictonary with user inputs
responses = {}
getting_Responses = True

while getting_Responses:
    name = input('what is your name?')
    car = input('what is your favourite car?')
    responses[name] = car
    repeat = input("Would you like to add another name?")
    if repeat == "no":
        getting_Responses = False

for name, response in responses.items():
    print(name.title() + " would like to have a " + response.title() + " one day.")

#--------------------------------------------------------------------------------------------------------------------------#
