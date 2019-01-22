#--------------------------------------------------------------------------------------------------------------------------#
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
#--------------------------------------------------------------------------------------------------------------------------#
#Basic statistics with a list of numbers
print(max(squares)) #Max value from the list
print(min(squares)) #Min value from the list
print(sum(squares)) #Sum of all the values in the list
#--------------------------------------------------------------------------------------------------------------------------#
#list Comprehension
squareV2 = [value**2 for value in range(1,11)]
print(squareV2)
#--------------------------------------------------------------------------------------------------------------------------#
#Working with part of a list
players = ['Claire', 'Dave', 'Steve','Matt', 'Jeff', 'Daniel']
print(players[0:2]) # will print part of the list index 0-2
print(players[1:4])#prints subset if the list 1 to range-1
print(players[:4])#prints upto player at range 4-1
print(players[2:])#prints all players after 3 in the list
print(players[-3:])#prints the last 3 players of the list and would function as size would change

#How to loop through a slice
print("Here are the players on my team")
for player in players[:3]:
    print("Lets go " + player.title())
#--------------------------------------------------------------------------------------------------------------------------#
#Copying a list
my_foods = ['pizza', 'pancakes', 'chicken', 'waffles']
friends_foods = my_foods[:]
print("My foods are:")
print(my_foods)
print("There foods are:")
print(friends_foods)
#--------------------------------------------------------------------------------------------------------------------------#
#Tuples
#Defining a Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

#Modifying a Tuple
dimensions = (30, 10) # new values in the tuple dimensions
for dimension in dimensions:
    print(dimension)
#--------------------------------------------------------------------------------------------------------------------------#
