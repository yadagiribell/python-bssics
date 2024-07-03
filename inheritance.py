class A:
    def method(self):
        print("A is defined as class")


class B:
    def method(self):
        print(" B is defined as class")


class C(A,B):
    def method(self):
        print("C class")
        super().method()

obj=C()
obj.method()