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
