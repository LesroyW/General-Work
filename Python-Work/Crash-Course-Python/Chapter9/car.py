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
