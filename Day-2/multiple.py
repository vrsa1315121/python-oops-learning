########## Multiple Inheritance ##############
class Father:
    def work(self):
        print("Father is working")
class Mother:
    def cook(self):
        print("Mother is Cooking")
class Child(Father,Mother):
    def play(self):
        print("Child is working")
c = Child()
c.work()
c.cook()
c.play()

################ Multiple Inheritance with __init__()
class Father:
    def __init__(self,house):
        self.house = house
    def show_house(self):
        print("House:",self.house)
class Mother:
    def __init__(self,car):
        self.car = car
    def show_car(self):
        print("Car:",self.car)
class Child(Father,Mother):
    def __init__(self,house,car):
        Father.__init__(self,house)
        Mother.__init__(self,car)
c = Child("Lucknow House","Honda")
c.show_house()
c.show_car()

########## Now Comes in MRO Methods ##########
class Father:
    def show(self):
        print("Father")
class Mother:
    def show(self):
        print("Mother")
class Child(Father,Mother):
    pass
c = Child()
c.show()
print(Child.mro())


####### Child
#  ↓
#Father
#  ↓
#Mother
#  ↓
#object

#python find show() in Father ,so it stops there.
##########/