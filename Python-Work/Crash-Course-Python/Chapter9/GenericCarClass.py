import car

my_bmw = car.Car("BWM", "1 series", 2012)
my_tesla = car.ElectricCarv2("Tesla", "Model s", 2019)

print(my_tesla.describe_car())
print(my_bmw.describe_car())


#not recommended to import all classes from module. can cause confusion within names
#from module_name import * - will cause potenital errors.
