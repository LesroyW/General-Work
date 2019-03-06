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
class IceCreamStand(Resturant2):
      def __init__(self, resturant_name, cuisine_type):
          super().__init__(resturant_name, cuisine_type)
          self.flavours = {"Chocolate", "Strawberry", "Vanilia"}

      def printflavours(self):
          print(self.flavours)

icecreamstand = IceCreamStand("Mick's Ice cream", "European")
icecreamstand.printflavours()

class Admin(User2):
      def __init__(self, firstname, lastname, age):
          super().__init__(firstname,lastname,age)
          self.privilages = Privilages()

class Privilages():
    def __init__(self):
        self.privilages = {"Can add post", "Can delete post", "Can Ban User"}

    def showPrivilages(self):
        for privilage in self.privilages:
            print(privilage)

admin = Admin( "John", "Mack", 203)
admin.privilages.showPrivilages()

class Car():
     def __init__(self, make, model, year):
         self.make = make
         self.model = model
         self.year = year
         self.odometer_reading = 0

     def read_odometer(self):
         print("This cars odometer is " + str(self.odometer_reading))

     def describe_car(self):
         long_name = "Make: " + self.make.title() + "\nModel: " + self.model.title() + "\nYear: " + str(self.year)
         return long_name.title()
#Modifying an attributes value
     def update_odometer(self, miles):
         if miles < self.odometer_reading or miles < 0:
             print("You can't roll back the miles buddy")
         else:
             self.odometer_reading = miles
#Incrementing an attributes value through a method
     def increment_odometer(self, miles):
         self.odometer_reading += miles

     def fill_gas_tank():
         print("Gas tank being filled!")

class Battery():
      def __init__(self, battery_size = 70):
          self.battery_size = battery_size

      def describe_battery(self):
          print("The size of this battery is " + str(self.battery_size) + " -Kwh battery.")

      def upgrade_battery(self):
          if self.battery_size != 85:
              self.battery_size = 85

      def get_range(self):
          if self.battery_size == 70:
              range = 240
          elif self.battery_size == 85:
              range = 300

          message = "This car has a range of: " + str(range) + " miles."
          print(message)




class ElectricCarv2(Car):
      def __init__(self, make,model,year):
          super().__init__(make,model,year)
          #Defining Attributes and methods for child class
          self.battery_size = Battery()

      #Overriding methods from the parent class
      def fill_gas_tank(self):
          print("This car doesn't need a gas tank!")

my_electric_car = ElectricCarv2("Mazda", "Hybrid", 2023)
my_electric_car.battery_size.get_range()
my_electric_car.battery_size.upgrade_battery()
my_electric_car.battery_size.get_range()

#--------------------------------------------------------------------------------------------------------------------------#
