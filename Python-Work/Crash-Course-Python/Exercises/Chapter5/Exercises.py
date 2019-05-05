#--------------------------------------------------------------------------------------------------------------------------#
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs car.upper == 'SUBARU'? I predict True.")
print(car.upper() == 'SUBARU')

age_2 = 50
print(age_2 > 30)
print(age_2 < 30)
print(age_2 >= 30 and age_2 <= 70)
print(age_2 > 60 or age_2 <= 50)

animals = ["Cat", "Dog","Mouse", "Bird"]
print('Mouse' in animals)
print('Lion' in animals)
animal = 'Lion'
if animal not in animals:
    print("YOU ARE NOT IN THE LIST. GOODBYE " + animal)
#--------------------------------------------------------------------------------------------------------------------------#
Alien_Colour = 'green'

if Alien_Colour == 'green':
    print("5 POINTS TO YOU PLAYER")

Alien_Colour = 'Yellow'
if Alien_Colour == 'green':
    print("OH NO WRONG ALIEN")

Alien_Colour = "Red"
if Alien_Colour == 'green':
    print("YOU HAVE EARNED 5 POINTS")
else:
    print("You have gained 10 points!")
#if version
if Alien_Colour == 'green':
    print("YOU HAVE EARNED 5 POINTS")
if Alien_Colour != 'green':
    print("You have gained 10 points!")

#elseif Version
if Alien_Colour == 'green':
    print("YOU HAVE EARNED 5 POINTS")
elif Alien_Colour == 'yellow':
    print("You have gained 10 points!")
elif Alien_Colour == 'red':
        print("You have gained 10 points!")

#Stages of life
age = 34
if age < 2:
    print("You are a baby")
elif age >= 2 and age < 4:
    print("You are a toddler")
elif age >= 4 and age < 13:
    print("You are a kid")
elif age >= 13 and age < 20:
    print("You are a teenager")
elif age >= 20 and age < 65:
    print("You are an adult")
elif age > 65:
    print("You are an elder")

favourite_fruit = ['Apple', 'Pinapple', 'Orange']
if 'Apple' in favourite_fruit:
    print("You really like Apples")
if 'Banana' in favourite_fruit:
    print("You really like Bananas")
#--------------------------------------------------------------------------------------------------------------------------#
usernames = ['David', 'Sam', 'Admin', 'Jeff', 'Matt']
if usernames:
    for username in usernames:
        if username == 'Admin':
            print("Hello " + username + " , would you like to see a satuts report?")
        else:
            print("Hello " + username + " , welcome to the site")
else:
    print("WE NEED TO FIND SOME USERS")

current_Users = ['David', 'Sam', 'Admin', 'Jeff', 'Matt']
new_users = ['Clarie', 'jeff', 'Sandra', 'Mark', 'Matt']
for new_user in new_users:
    if new_user.title() in current_Users:
        print("You will need a new username " + new_user)
    else:
        print("This username is available")
#--------------------------------------------------------------------------------------------------------------------------#
#Ordinal numbers
numbers = [1, 5,6,7,8,3,9,4,2]
numbers.sort()
for number in numbers:
    if number > 3:
        print(str(number)+"th")
    elif number == 3:
        print(str(number)+"rd")
    elif number == 2:
        print(str(number)+"nd")
    elif number == 1:
        print(str(number)+"st")

#--------------------------------------------------------------------------------------------------------------------------#
