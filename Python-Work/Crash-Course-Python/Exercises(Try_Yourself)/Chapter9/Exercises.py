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
class Resturant2():

    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_resturant(self):
        print("The name of the resturant is " + self.resturant_name + " the cuisine server is " + self.cuisine_type + " it currently has served: " + str(self.number_served) + " customers" )

    def open_resturant(self):
        print("The resturant is open!")

    def increment_number_served(self, amount_served):
        self.number_served += amount_served

resturant = Resturant2("Big Joes", "Thai")
resturant.describe_resturant()
resturant.increment_number_served(23)
resturant.describe_resturant()

class User2():

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print("This users name is " + self.firstname + " " + self.lastname + " and their age is " + str(self.age))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def print_login_attempts(self):
        print(str(self.login_attempts))

user = User2("Jack", "Matt", 34)
user.increment_login_attempts()
user.print_login_attempts()
user.reset_login_attempts()
user.print_login_attempts()
#--------------------------------------------------------------------------------------------------------------------------#
