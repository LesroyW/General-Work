pizzas = ["Pepperoni", "Cheese", "Ham"]
tabs = "";
for pizza in pizzas:
    print(tabs + "I love " + pizza + " pizza.")
    tabs += "\t"

print("I love pizza as it is great.\nMany combinations and tastes.\nYou should try it one day.\nI really love pizza!")


animals = ["Cat", "Dog", "Mouse"]
for animal in animals:
    print("A " + animal.lower() + ", would make a great pet")

print("Any of thses animals would make a great pet")
#-------------------------------------------------------------------------------------------#
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
