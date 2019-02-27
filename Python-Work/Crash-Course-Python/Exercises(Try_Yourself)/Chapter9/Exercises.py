#--------------------------------------------------------------------------------------------------------------------------#
class Resturant():

    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type

    def describe_resturant(self):
        print("The name of the resturant is " + self.resturant_name + " the cuisine server is " + self.cuisine_type)

    def open_resturant(self):
        print("The resturant is open!")

my_resturant = Resturant("Maccie d's", "Thai")
print(my_resturant.resturant_name.title())
print(my_resturant.cuisine_type)
my_resturant.describe_resturant()
my_resturant.open_resturant()

my_resturant2 = Resturant("KFC", "Spanish")
my_resturant3 = Resturant("Pepe's", "Italian")

my_resturant2.describe_resturant()
my_resturant3.describe_resturant()

class User():

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def describe_user(self):
        print("This users name is " + self.firstname + " " + self.lastname + " and their age is " + str(self.age))

user1 = User("Mark", "Matt", 5)
user2 = User("Sam", "Samson", 23)
user3 = User("Jeff", "Jefferson" , 34)

user1.describe_user()
user2.describe_user()
user3.describe_user()
#--------------------------------------------------------------------------------------------------------------------------#
