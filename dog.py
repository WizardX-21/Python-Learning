class Dog:
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

# Creating an instance of Dog
my_dog = Dog('Willie', 6)

# Accessing attributes and calling methods
print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog's age is {my_dog.age}.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy',3)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
