#--------------------------------------------------------------------------------------------------------------------------#
def greet_user(username):
    """Display a simple greeting."""
    print("Hello! " + username.title())

greet_user("mark")


#positionalArguements
def describe_pet(animal_type, pet_name):
    print("\n I have a "+ animal_type + ".")
    print("My " + animal_type + " is called " + pet_name.title())

#can call function as many times as possible
#Problems can occur if wrong inputs given to parameters
#--------------------------------------------------------------------------------------------------------------------------#
#Can use key word arguements for parameters
describe_pet(pet_name= "Mark", animal_type= "Zebra")
#--------------------------------------------------------------------------------------------------------------------------#
#Using default values for functions
def describe_location(city, country="England"):
    print("My country is " + country)
    print("My city is " + city)

describe_location("Birmingham")
describe_location("Barcalona", "Spain")
#Ignores default value
#describe_location() this would produce an error as the function call is not containing the correct amount of parameters 
#--------------------------------------------------------------------------------------------------------------------------#
