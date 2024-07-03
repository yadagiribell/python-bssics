class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def show(self):
        print(self.name,self.rollno)



    class Laptop:
        def __init__(self,brand,cpu):
            self.brand=brand
            self.cpu=cpu
        def show(self):
            print(self.brand,self.cpu)
s1=student("ram",501)
s1.show()
lap1=student.Laptop("hp","i5")
lap1.show()


