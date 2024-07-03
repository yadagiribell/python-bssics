class Animal:
    def eat(self):
        print("eating")
class Dog(Animal):
    def bark(self):
        print("barking")
d=Dog()
d.bark()
d.eat()