#--------------------------------------------------------------------------------------------------------------------------#
prompt = "What kind of rental car would you like."
car = input(prompt)
print("Let me see if we can get you a " + car)

prompt = "How many people are going to be with you? "
amountOfPeople = input(prompt)

if int(amountOfPeople) > 8:
    print("I'm sorry we cannot sit that many people.")
else:
    print("Right this way!")

prompt = "I can check if the number you enter is a multiple of 10: "
number = input(prompt)
if int(number) % 10 == 0:
    print(str(number) + "is a multiple of 10")
else:
    print(str(number) + "is not a multiple of 10")
#--------------------------------------------------------------------------------------------------------------------------#
