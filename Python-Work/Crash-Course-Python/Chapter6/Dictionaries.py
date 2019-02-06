#--------------------------------------------------------------------------------------------------------------------------#
alien_0 = { 'color' : 'green', 'points' : 5}
#example of dictionary
#Similar to Hashmaps
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You have earn "+ str(new_points) + " points!")

#adding new key-value pairs
alien_0['x-position'] = 0
alien_0['y-position'] = 25

print("The position of the Alien is " + "x:" + str(alien_0['x-position']) + " y:"+ str(alien_0['y-position']))

#empty dictionary
alien_0 = {}
#--------------------------------------------------------------------------------------------------------------------------#
#Modifying values within a dictionary
alien_0 = { 'color' : 'green', 'points' : 5}
alien_0['points'] = 20

print("You have earn "+ str(alien_0['points']) + " points!")

#Demo
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'fast':
    x_increment = 3
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'slow':
    x_increment = 1

alien_0['x_position'] += x_increment

print("New x-position of alien: " + str(alien_0['x_position']))
#--------------------------------------------------------------------------------------------------------------------------#
#Removing Key-value pairs
del alien_0['y_position']
print(alien_0)
#--------------------------------------------------------------------------------------------------------------------------#
#dictionary of similar objects
favorite_languages = {    'jen': 'python',
  'sarah': 'c',
   'edward': 'ruby',
     'phil': 'python',
       }
print("Phils favorite programming language is " + favorite_languages['phil'].title() + ".")
#--------------------------------------------------------------------------------------------------------------------------#
#looping through a dictionary
#looping through key and values
for key, value in favorite_languages.items():
    print(key + " : " + value)

#looping through key
for key in favorite_languages.keys():
    print(key.title())

#simipler way:
for key in favorite_languages:
    print(key.title())

#Looping through with if statements

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
     print(name.title())
     if name in friends:
                print("  Hi " + name.title() + ", I see your favorite language is " +  favorite_languages[name].title() + "!")

#CHecking if person is not list
if 'Matt' not in favorite_languages.keys():
    print("Please take our survey Matt")
#prints keys in sorted order
for key in sorted(favorite_languages.keys()):
    print(key.title())

#Looping through the values within a list
for value in sorted(favorite_languages.values()):
    print(value.title())

#getting unique items if you wrap set around collection
for value in sorted(set(favorite_languages.values())):

    print("\t" + value.title())
#--------------------------------------------------------------------------------------------------------------------------#
#List of Dictionaries
alien_0 = {'color' : 'red', 'points' : 4}
alien_1 = {'color' : 'green', 'points' : 12}
alien_2 = {'color' : 'blue','points' : 18}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    for value in alien.values():
        print(str(value))

aliens = []

for alien_number in range(30):
     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
     aliens.append(new_alien)

for alien in aliens[:10]:
    print(alien)

print("There are " + str(len(aliens)) + " aliens still alive." )

for alien in aliens[::5]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['points'] = 30
        alien['speed'] = 'fast'
for alien in aliens:
    print(alien)
#--------------------------------------------------------------------------------------------------------------------------#
#List within a dictionary
pizza = { 'crust' : 'thick' , 'toppings' : ['cheese', 'tomato', 'pineapple']}
print("You order a " + pizza['crust'] + " crust pizza " + " with the following toppings:")
for value in pizza['toppings']:
    print(value.title())

languages = { 'Dave' : ['ruby', 'java'], 'Matt' : ['java', 'Python'],
'Jen' : ['C#','Haskell'], }

for name, languages in languages.items():
    print(name.title() + " likes:")
    for language in languages:
        print("\t" + language.title())

#--------------------------------------------------------------------------------------------------------------------------#
#dictionary within a dictionary
people = { 'dave' : {'Gender' : 'male','Age' : 22, 'Occupation' :"Programmer"}
}
print(people)
for username, user_info in people.items():
    print(username + user_info['Gender'])
    fullDetails = username + " , " +user_info['Gender'] + " , " + str(user_info['Age'])+ " , " + user_info['Occupation']
print(fullDetails)
#--------------------------------------------------------------------------------------------------------------------------#
