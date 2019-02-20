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
#Return values
def get_formatted_name(first_name, last_name):
    """return a full name, neatly formatted."""
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name("Mark", "Daniels")
print(musician)

def get_formatted_name_with_middle_name(first_name, last_name, middle_name =''):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name_with_middle_name("Mark", "Daniels", "Samuel")
print(musician)
#--------------------------------------------------------------------------------------------------------------------------#
#Returning a Dicitionary

def build_person(first_name, last_name):
    """Return a Dicitionary"""
    person = {'first' : first_name, 'last' : last_name}
    return person

musician = build_person("Mark", "Samuel")
print(musician)

def build_person_with_age(first_name, last_name, age=""):
    """Return a Dicitionary"""
    person = {'first' : first_name, 'last' : last_name}
    if age:
        person['age'] = age
    return person

musician = build_person_with_age("Mark", "Samuel", '34')
musicanB = build_person_with_age("Mark", "Ramuel")
print(musician)
print(musicanB)
#--------------------------------------------------------------------------------------------------------------------------#
#Using a function within a loop:
while True:
    print("Tell me your name?")
    f_input = input("First name: ")
    l_input = input("Last name: ")
    toReturn = get_formatted_name(f_input, l_input)
    print("Hello " + toReturn + "!")
    q_input = input("Do you want to quit?")
    if(q_input == "q"):
        print("Ok Leaving....")
        break
#--------------------------------------------------------------------------------------------------------------------------#
#Passing a Lists

def greet_users(names):
    for name in names:
        print("Hello " + name.title() + " nice to meet you!")

usernames = ["Mark", "jeff", "sam"]
greet_users(usernames)

#Modifying a Lists


def printModels(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Currently printing " + current_design)
        completed_models.append(current_design)

def completed_Models_printed(completed_models):
    for completed_model in completed_models:
        print(completed_model + " has been completed.")

unprinted_designs = ["Crab", "Hook", "Mask"]
completed_models = []

printModels(unprinted_designs, completed_models)
completed_Models_printed(completed_models)

#def printModels(unprinted_designs[:], completed_models)
#This would prevent the list being Modified and becoming empty and unusable


#--------------------------------------------------------------------------------------------------------------------------#
