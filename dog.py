class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is %s." % my_dog.name.title())
print("My dog is %i years old." % my_dog.age)
my_dog.sit()

print("\nYour dog's name is %s." % your_dog.name.title())
print("Your dog is %i years old." % your_dog.age)
your_dog.sit()
