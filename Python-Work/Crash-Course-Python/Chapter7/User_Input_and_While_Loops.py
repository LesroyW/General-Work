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
