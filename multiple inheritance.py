class Animal:
    def eat(self):
        print("eating")
class Dog(Animal):
    def bark(self):
        print("barking")
class Cat(Animal):
    def meow(self):
        print("meow meow")

c=Cat()
c.meow()
c.eat()
