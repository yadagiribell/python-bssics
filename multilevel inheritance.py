class Animal:
    def eat(self):
        print("eating")
class Dog(Animal):
    def bark(self):
        print("barking")
class Babydog(Dog):
    def weep(self):
        print("weeping")
b=Babydog()
b.weep()
b.eat()
b.bark()
