class Animal:
    alive = True

    def eat(self):
        print("the animal is eating")
    def slumber(self):
        print("this animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("the rabbit is running")

class Fish(Animal):
    def swim(self):
        print("the fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("the hawk is flying")

rabbit = rabbit()
fish = fish()
hawk = hawk()

rabbit.run()
fish.swim()
hawk.fly()