#--------------------------------------------------------------------------------------------------------------------------#
#Basic use of if statment
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if(car == 'bmw'):
        print(car.upper())
    else:
        print(car.title())
#Checks whether the value in car matches to bmw and executs appropriately
#--------------------------------------------------------------------------------------------------------------------------#
#Conditional tests
#Basic Conditional test 3 == 3 or 3 = 3
#Checking for equality   C = 'audi'  C == 'bmw' would retun false
#case is also ignore when checking for equality would have to use .lower()/.upper() depending of value
#!= can be used to check for inequality

#Numerical Comparisons
#Much simipler age = 18    age == 18  would return True
#Can do the same if two numbers are not equal
#Can do mathematical comparisons as well such as <,>,>=,<=

#Checking multiple conditions using the and/or key word
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 20 or age_1 >= 35)
#--------------------------------------------------------------------------------------------------------------------------#
#Checking whether a value is in a list
#Use the key word in to find this out
requested_toppings = ['cheese', 'mushroom', 'tomato']
print('cheese' in requested_toppings)
print('Pork' in requested_toppings)
#--------------------------------------------------------------------------------------------------------------------------#
#Indention with if statements
#Everything indented within if statement gets executed
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
#Everything above will be executed as the condition is met
#--------------------------------------------------------------------------------------------------------------------------#
#If-else statements
#Else is what will be executed if the condition isn't met
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
#This section will print out the else statment as the condition hasn't been met
#--------------------------------------------------------------------------------------------------------------------------#
#using Elif(else-if)
#Using this will allow for the multi-chaining of several condtion statements
#Will be used in a similar way as if it was the if portion itself
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
elif age < 60:
    print("Your admission cost is $20")
else:
    print("Your admission cost is $10.")
#Will print out the secondary condition as the statement is met there
#--------------------------------------------------------------------------------------------------------------------------#
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")
#Breaks out of else if statement once condition is met
#Else will take anything that isn't met bad data or invalid input
#Use elseif when not wanting to encounter these
#--------------------------------------------------------------------------------------------------------------------------#
#Can use multiple if statements as else if statments breaks out once condition mathematical
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
    print("\nFinished making your pizza!")

#Compared to:
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
    print("\nFinished making your pizza!")

#--------------------------------------------------------------------------------------------------------------------------#
