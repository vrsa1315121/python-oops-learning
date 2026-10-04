############# Operator Overloading #############
#Giving an operator different behavior depending on the objects being used.
class Student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,others):
        return self.marks + others.marks

s1 = Student(80)
s2 = Student(100)
print(s1+s2)

class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def __add__(self,others):
        return self.balance + others.balance

b1 = BankAccount(1000)
b2 = BankAccount(3000)

print(b1 + b2)

