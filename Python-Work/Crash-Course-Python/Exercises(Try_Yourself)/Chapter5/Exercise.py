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
