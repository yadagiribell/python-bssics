from threading import *
from time import sleep
class yadagiri(Thread):
    def run(self):
        for i in range(30):
            print("yadagiri")
            sleep(1)

class shekar(Thread):
    def run(self):
        for i in range(30):
            print("shekar")
            sleep(1)
t1=yadagiri()
t2=shekar()
t1.start()
sleep(0.2) #sleep is used to for waiting threads execution between them
t2.start()
t1.join()   #join is used until t1 and t2 executes main thread will execute
t2.join()

print("bye")  #executed by main thread