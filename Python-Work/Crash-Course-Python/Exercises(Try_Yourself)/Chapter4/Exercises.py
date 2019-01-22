pizzas = ['Pepperoni', 'Cheese', 'Ham', 'Bacon', 'Pinapple', 'Beef', 'Lamb']
tabs = "";
for pizza in pizzas:
    print(tabs + "I love " + pizza + " pizza.")
    tabs += "\t"

print("I love pizza as it is great.\nMany combinations and tastes.\nYou should try it one day.\nI really love pizza!")


animals = ["Cat", "Dog", "Mouse"]
for animal in animals:
    print("A " + animal.lower() + ", would make a great pet")

print("Any of thses animals would make a great pet")
#--------------------------------------------------------------------------------------------------------------------------#

for value in range(1,21):
    print(value)

oneToOneThousand = []
for value in range(1,1001):
    oneToOneThousand.append(value)

print(min(oneToOneThousand))
print(max(oneToOneThousand))
print(sum(oneToOneThousand))

for value in range(1, 20, 2):
    print(value)

for value in range(3, 32,3):
    print(value)

for value in range(1, 11):
    print(value**2)

cubed = [value**3 for value in range(1, 10)]
for cube in cubed:
    print(cube)
#--------------------------------------------------------------------------------------------------------------------------#
print("The first 2 items in the pizza list are: ")
for pizza in pizzas[:2]:
    print(pizza)

print("The items from the middle of the list onwards are: ")
for pizza in pizzas[3:]:
    print(pizza)

print("The last three items in the list is: ")
for pizza in pizzas[-3:]:
    print(pizza)

friends_pizzas = pizzas[:]
pizzas.append('Spicy')
print('My favourite pizzas are:')
for pizza in pizzas:
    print("\t" + pizza)

print('My friends favourite pizzas are:')
for pizza in friends_pizzas:
    print("\t" + pizza)
#--------------------------------------------------------------------------------------------------------------------------#
#Tuples
Buffet = ('Bread', 'Pizza', 'Cheese', 'Ham', 'Bacon')
for item in Buffet:
    print(item)

#Buffet[2] = "Fish" Breaks the system

Buffet = ('Bread', 'Beef', 'Cheese', 'Ham', 'Pasta')
for item in Buffet:
    print(item)
