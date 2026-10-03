class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
dog = Dog()
dog.eat()
dog.bark()

########## Employee -> Developer ##########
class Employee:
    def work(self):
         print("Employee is working")
class Developer(Employee):
     def code(self):
         print("Developer is coder")
dev = Developer()
dev.work()
dev.code()

############  Inhritance with init ############
class Employee:
        def __init__(self,name):
            self.name = name
        def display(self):
             print("Name:",self.name)
class Developer(Employee):
        def code (self):
             print(self.name,"is coder")
dev = Developer("vinay")
dev.display()
dev.code()
