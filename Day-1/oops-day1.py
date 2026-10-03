class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
         return f"{self.name} says woof, age is {self.age}"

# Create object of Class Dog
d = Dog("Rex",3)
d1 = Dog("Bella",5)

print(d.bark())

######### Take one more Example ###############
class Employee:
    def __init__(self,name):
        self.name = name
    def display(self):
            return f"Employee name is {self.name}"
emp = Employee("Vinay")
print(emp.display())