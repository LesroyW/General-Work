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
