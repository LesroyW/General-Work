#--------------------------------------------------------------------------------------------------------------------------#
#Basic Dog class
class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

#Creates Dog and assigns it to the my_dog variable
my_dog = Dog("Sam", 2)
#Uses the sit function from dog class
my_dog.sit()
print(my_dog.name.title() + " is " + str(my_dog.age) + " years old.")
#--------------------------------------------------------------------------------------------------------------------------#
#Calling multiple instances
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
#--------------------------------------------------------------------------------------------------------------------------#
#Working with Classes and instances
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

my_new_car = Car("Ferrari", "Spider", 2009)
print(my_new_car.describe_car())
my_new_car.read_odometer()
my_new_car.update_odometer(6)
my_new_car.read_odometer()
my_new_car.update_odometer(-2)
my_new_car.increment_odometer(400)
my_new_car.read_odometer()

#--------------------------------------------------------------------------------------------------------------------------#
#Using Inheritence within python
class Electriccar(Car):
      def __init__(self, make,model,year):
          super().__init__(make,model,year)
          #Defining Attributes and methods for child class
          self.battery_size = 90

      def describe_battery(self):
          print("This car has a " + str(self.battery_size) + " -kwh battery.")

      #Overriding methods from the parent class
      def fill_gas_tank(self):
          print("This car doesn't need a gas tank!")



my_new_car = Electriccar("Tesla", "Roadster", 2018)
print(my_new_car.describe_car())
my_new_car.describe_battery()
my_new_car.fill_gas_tank()
#--------------------------------------------------------------------------------------------------------------------------#
#Instances as attributes
class Battery():
      def __init__(self, battery_size = 70):
          self.battery_size = battery_size

      def describe_battery(self):
          print("The size of this battery is " + str(self.battery_size) + " -Kwh battery.")

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

my_bmw = ElectricCarv2("BMW", "electricbwm", 2020)
my_bmw.battery_size.describe_battery()
my_bmw.battery_size.get_range()
#--------------------------------------------------------------------------------------------------------------------------#
#Importing Classes
#--------------------------------------------------------------------------------------------------------------------------#
