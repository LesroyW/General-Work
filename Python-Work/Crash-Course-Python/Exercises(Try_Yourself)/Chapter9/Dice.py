from random import randint

class Dice():
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        x = randint(1,self.sides)
        print(str(x))

my_die = Dice()
my_die.roll_die()
my_new_Die = Dice(10)
my_new_Die.roll_die()
my_new_new_Die = Dice(20)
my_new_new_Die.roll_die()
