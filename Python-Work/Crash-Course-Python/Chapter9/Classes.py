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
