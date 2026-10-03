# Multilevel Inheritance
class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    def bark(self):
        print("Barking")
class Puppy(Dog):
    def play(self):
        print("Playing")
p  = Puppy()
p.eat()
p.bark()
p.play()

# More Example
class Vehicle:
    def __init__(self,brand):
        self.brand = brand
    def show_brand(self):
        print("Brand:",self.brand)
class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model = model
    def show_model(self):
        print("Model:",self.model)
class ElectricCar(Car):
    def __init__(self,brand,model,battery):
        super().__init__(brand,model)
        self.battery = battery
    def show_battery(self):
        print(f"Battery: {self.battery} KWh")
el = ElectricCar("Tesla","Model 3",75)
el.show_brand()
el.show_model()
el.show_battery()

#### one more example #########

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_person(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary
    def show_salary(self):
        print("Salary:",self.salary)
class Manager(Employee):
    def __init__(self,name,age,salary,team_size):
         super().__init__(name,age,salary)
         self.team_size = team_size
    def show_manager(self):
        print("Team Size:",self.team_size)
m = Manager("Vinay",30,80000,10)
m.show_person()
m.show_salary()
m.show_manager()

############# User ##############
class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email
    def show_user(self):
        print("Username:",self.username)
        print("Email:",self.email)
class Employee(User):
    def __init__(self,username,email,employee_id,salary):
        super().__init__(username,email)
        self.employee_id = employee_id
        self.salary = salary
    def show_emp(self):
        print("Employee Id :",self.employee_id)
        print("Salary:",self.salary)
class Developer(Employee):
    def __init__(self,username,email,employee_id,salary,programming_language,experience):
        super().__init__(username,email,employee_id,salary)
        self.programming_language = programming_language
        self.experience = experience
    def show_dev(self):
        print("Programming Lanaguage:",self.programming_language)
        print(f"Experience {self.experience} years")
d = Developer("Vinay","vinay@gmail.com",101,90000,"Python",3)
d.show_user()
d.show_emp()
d.show_dev()
