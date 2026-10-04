################ Basic Polymorphism ############
class Animal:
    def sound(self):
        print("Animal Makes Sound")
class Dog(Animal):
    def sound(self):
        print("Dog is barking")

animal = Animal()
animal.sound()
dog = Dog()
dog.sound()