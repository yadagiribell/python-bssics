class student:
    def __init__(self,rno,name):
        self.rno=rno
        self.name=name
    def details(self):
        print(self.rno,self.name)
std1=student("ram",501)
std2=student("sreekanth",510)
std3=student("yadagiri",503)
std1.details()
std2.details()
std3.details()

