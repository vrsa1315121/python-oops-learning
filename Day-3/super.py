################## super() + Method Overriding ############
######### super() is used to access methods or attributes of a parent class.

class Employee:
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def work(self):
        super().work()
        print("Developer is working")
dev = Developer()
dev.work()
