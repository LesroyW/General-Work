#----------------------------------------------------------------------------------------------#
#Looping within a list
magicians = ['alice', 'micheal', 'matt']
#For loop to print out a list
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician.title() + ", is the greatest magician")
    print(magician.title() + ", great things are to come. \n")

print("Thank you everyone for attending")

#Always indent when using a for loop in python. Indent out when finished using the loop

for value in range(0,5):
     print(value)
#prints 1 to range - 1

for value in range(1,6):
    print(value)
#prints 1 - 5

#make list of numbers
numbers = list(range(0,200))
#numbers between 0 - 199

even_numbers = list(range(2,11,2))
print(even_numbers)
#only prints even numbers second 2 is the amount to increment in the list

squares = []
for value in range(2,11):
    number = value**2
    squares.append(number)

print(squares)
#squares the numbers within the range 2 - 11 and adds it to the list squares

#more simple way would be: removes and extra line
squares = []
for value in range(2,11):
    squares.append(value**2)

print(squares)
#-------------------------------------------------------------------------------------------#
#Basic statistics with a list of numbers
print(max(squares)) #Max value from the list
print(min(squares)) #Min value from the list
print(sum(squares)) #Sum of all the values in the list
#-------------------------------------------------------------------------------------------#

#list Comprehension
squareV2 = [value**2 for value in range(1,11)]
print(squaresV2)
#-------------------------------------------------------------------------------------------#
#Working with part of a list
