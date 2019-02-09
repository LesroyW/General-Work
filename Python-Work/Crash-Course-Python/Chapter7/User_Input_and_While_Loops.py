#--------------------------------------------------------------------------------------------------------------------------#
#Basic user input
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#Input prompt should be clear and easy
name = input("Please enter your name: ")
print("Hello " + name + "!")

prompt = "We are first going to learn your name."
prompt += "\nWhat is your name: "
name = input(prompt)
print("Hello " + name + "!")

#All inputs are interpreted as a string.
prompt = "What is your age? "
age = input(prompt)
print( int(age) >= 20)
#--------------------------------------------------------------------------------------------------------------------------#
