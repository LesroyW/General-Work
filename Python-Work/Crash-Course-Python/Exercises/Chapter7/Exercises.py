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

prompt = "What are your favourite toppings: "

toppingToPrint = ""
while toppingToPrint != "Quit":
    toppingToPrint = input(prompt)
    if toppingToPrint != 'Quit':
        print("I will add " + toppingToPrint)
    else:
        break

prompt = "How old are you?"
age = ""
while age != 'Quit':
    age = input(prompt)
    if str(age) == "Quit":
        break
    if int(age) < 3:
        print("Free of charge")
    elif int(age) >= 3 and int(age)< 13:
        print("£10 for ticket")
    else:
        print("£15 for ticket")

prompt = "What are your favourite toppings: "

toppingToPrint = ""
active = True
while active:
    toppingToPrint = input(prompt)
    if toppingToPrint == 'Quit':
        active = False
    else:
        print("I will add " + toppingToPrint)
#--------------------------------------------------------------------------------------------------------------------------#
