# Super Method call in inheritance 
class Employee:
    def __init__(self,name):
        self.name = name
class Developer(Employee):
     def __init__(self,name,language):
         super().__init__(name)
         self.language = language
dev = Developer("Vinay","Python")
print(dev.name)
print(dev.language)

# Using Methods
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
class Developer(Employee):
    def __init__(self,name,salary,language):
        super().__init__(name,salary)
        self.language = language
    def show_language(self):
        print("Language:",self.language)
dev = Developer("Vinay",120000,"Python")
dev.display()
dev.show_language()


