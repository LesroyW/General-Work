#--------------------------------------------------------------------------------------------------------------------------#
my_Info = {'Age' : 20, 'Nationality' : 'British', 'City' : 'Birmingham', 'Sport' : 'Football'}
for key, value in my_Info.items():
    print(str(key) + ' : ' + str(value))

favourite_numbers = {'dave' : 2, 'Kerry' : 6, 'malcom' : 8, 'Sam' : 90}
for key, value in favourite_numbers.items():
    print(key.title() + " favourite number is : " + str(value))

glossary_Defintions = {
'car' : 'a road vehicle, typically with four wheels, powered by an internal combustion engine and able to carry a small number of people.', 'bike' : 'a bicycle or motorcycle.', 'person' : 'a human being regarded as an individual.'
}

for key, value in glossary_Defintions.items():
    print("Word: " + key + '\nDefintion: ' + value)
#--------------------------------------------------------------------------------------------------------------------------#
rivers = {'nile' : 'egypt', 'amazon' : 'brazil', 'Thames' : 'The United Kingdom'}
for key , value in rivers.items():
    print("The " + key.title() + " runs through " + value.title())

for key in rivers.keys():
    print("The rivers are: " + key)

for value in rivers.values():
    print("The countries are: " + value)

if 'Congo River' not in rivers.keys():
    print("The congo river should be added")

if 'Venice' not in rivers.values():
    print("HOW IS VENICE NOT HERE IT IS LITERALLY THE CITY OF RIVERS")
#--------------------------------------------------------------------------------------------------------------------------#
