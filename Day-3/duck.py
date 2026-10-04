##### Python cares about what an object can do, rather than what class it belongs to.
class Car:
    def start(self):
        print("Car Started")
class Bike:
    def start(self):
        print("Bike Started")

def start_vechile(vechile):
    vechile.start()

start_vechile(Car())
start_vechile(Bike())


class Dog:
    def sound(self):
        print("Dog Barks")
class Cat:
    def sound(self):
        print("Cat meows")
class Cow:
    def sound(self):
        print("Cow Moos")
def make_sound(animal):
    animal.sound()

make_sound(Dog())
make_sound(Cat())
make_sound(Cow())
