#--------------------------------------------------------------------------------------------------------------------------#
def display_message():
    print("This is Awesome")

display_message()

def favourite_book(bookTitle):
    print("Your favourite book is " + bookTitle.title())
#--------------------------------------------------------------------------------------------------------------------------#
def make_shirt(size, textOnShirt):
    print("Your sized shirt is " + str(size) + " and the text on the shirt will be: " + textOnShirt)

make_shirt(3, "Hi its me")

make_shirt(textOnShirt ="WOOW!" , size = 43)

def make_shirt(size, textOnShirt = "I love python!"):
        print("Your sized shirt is " + size + " and the text on the shirt will be: " + textOnShirt)

make_shirt("Large")

def describe_city(city, country= "England"):
    print(city + " is in " + country)

describe_city("Birmingham")
describe_city("London")
describe_city("Venice")
#--------------------------------------------------------------------------------------------------------------------------#
def describe_country(city, country):
    country_details = { "City" : city, 'Country': country}
    print(country_details)

describe_country("Berlin", "Germany")
describe_country("Paris", "France")
describe_country("New York", "USA")

def make_album(artist_name, album_title, tracks=""):
    album_details = {'Artist' : artist_name, "Album" : album_title}
    if tracks:
        album_details['tracks'] = tracks
    print(album_details)

make_album("Jay Lo", "something")
make_album("Jay Z", "Otis" )
make_album("Anderson .Paak", "Oxnard", "12")

def make_album(artist_name, album_title, tracks=""):
    album_details = {'Artist' : artist_name, "Album" : album_title}
    if tracks:
        album_details['tracks'] = tracks
    return album_details

while True:
    artist = input("Artist name: ")
    album = input("Album name: ")
    tracks = input("Amount of tracks: ")
    make_album = make_album(artist, album, tracks)
    print(make_album)
    quit = input("Do you want to quit? ")
    if(quit == "q"):
        break
#--------------------------------------------------------------------------------------------------------------------------#
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

list_of_magicians = ["Penn", "Teller", "David Blaine"]
show_magicians(list_of_magicians)

def make_great(magicians, NewMagicians):
    for magician in range(0,len(magicians)):
        current_Magician = magicians.pop()
        current_Magician += " the Great"
        NewMagicians.append(current_Magician)
    return NewMagicians

list_of_magicians = ["Penn", "Teller", "David Blaine"]
NewMagicians = []
make_great(list_of_magicians[:], NewMagicians)
show_magicians(NewMagicians)
show_magicians(list_of_magicians)

def sandwhiches_wanted(*fillings):
    for filling in fillings:
        print("You want " + filling + " in your sandwhich")
sandwhiches_wanted("Milk", "Tomato")
sandwhiches_wanted("Cheese")
sandwhiches_wanted("Pork", "Beef", "Salom")

def build_profile(first_name, last_name, **user_info):
    profile = {}
    profile['first_name'] = "Mark"
    profile['last_name'] = "Sam"
    for key, value in user_info.items():
        profile[key] = value
    return profile

my_profile = build_profile("Lesroy", "Wedderburn", Age = "20", Height = "5'10")
print(my_profile)

def make_car(manufacturer, model_name, **car_info):
    carInfo = {}
    carInfo["manufacturer"] = manufacturer.title()
    carInfo['model_name'] =model_name.title()
    for key, value in car_info.items():
        carInfo[key] = value
    return carInfo

newCar = make_car("Nissan", "Micra", Colour ="Blue", Lenght= "5 feet")
print(newCar)
#--------------------------------------------------------------------------------------------------------------------------#
