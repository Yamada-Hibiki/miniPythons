class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("Don't know man")

# pet1 = Pet("Tim", 19)
# cat1 = Cat("Bill", 34, "red")
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)  # pass the arguments name and age from the super class "Pet", not to miss some info
        self.color = color  # We can't just ignore upper class __init__

    def speak(self):
        print("Meow")

    # def show(self):
    #     print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")


class Dog(Pet):
    def speak(self):
        print("Bark")


pet1 = Pet("Tim", 19)
cat1 = Cat("Bill", 34, "red")
dog1 = Dog("Jill", 25)

print(pet1.show())
