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
         if miles < self.odometer_reading:
             print("You can't roll back the miles buddy")
         else:
             self.odometer_reading = miles
#Incrementing an attributes value through a method

my_new_car = Car("Ferrari", "Spider", 2009)
print(my_new_car.describe_car())
my_new_car.read_odometer()
my_new_car.update_odometer(6)
my_new_car.read_odometer()
my_new_car.update_odometer(2)


#--------------------------------------------------------------------------------------------------------------------------#
