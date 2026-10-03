# Overriding methods in python oops concepts
# Animal makes sound Dog Barks overrides the parent versions
class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog Barks")

animal = Animal()
dog = Dog()
animal.sound()
dog.sound()

# super() methods with Method Overriding
class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog Barks")
dog = Dog()
dog.sound()

# Super() methods with method overriding
class Employee:
     def work(self):
         print("Employee is working")
class Developer(Employee):
    def work(self):
        super().work()
        print("All developer is working")
dev = Developer()
dev.work()

