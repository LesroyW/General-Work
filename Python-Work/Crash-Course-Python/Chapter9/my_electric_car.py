from car import ElectricCarv2, Car

my_car = ElectricCarv2("Tesla", "Roadster", 2020)
print(my_car.describe_car())
my_car.battery_size.describe_battery()
my_car.battery_size.get_range()

my_other_car = Car("Ferrari", "Spider", 2001)
print(my_other_car.describe_car())
