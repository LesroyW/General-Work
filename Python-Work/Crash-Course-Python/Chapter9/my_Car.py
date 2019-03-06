#Importing from a different class
from car import Car
my_new_car = Car("Audi", "A4", 2015)
print(my_new_car.describe_car())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
