############# Overriding Polyporpshim #############

class CreditCard:
    def pay(self):
        print("Payment using credit card")
class UPI:
    def pay(self):
        print("Payment using UPI")
class Paypal:
    def pay(self):
        print("Payment using paypal")

card = CreditCard()
upi = UPI()
paypal = Paypal()

card.pay()
upi.pay()
paypal.pay()

############### Polymorphsim Overriding ###############

class Employee:
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def work(self):
        print("Developer is working")
class Manager(Employee):
    def work(self):
        print("Manager is working")

dev = Developer()
man = Manager()
dev.work()
man.work()

