'''
thread is a sub program of the process or thread is individual part of a proccess
process is program under execution
process is heavy weight while thread is light weight process
every process will alloccate separate memory while every thread will allocate common memeory


thread methods
start()
join()
sleep(0.1 t0 1.0)
run()
synchronized()



'''
import threading
import time


def f_sqaure(num):

    for n in num:
        time.sleep(0.5)
        print("sqaure=",n*n)
def f_cube(num):
    for n in num:
        time.sleep(0.7)
        print("cube=",n*n*n)
arr=[1,2,3,4]
t1=threading.Thread(target=f_sqaure,args=(arr,))
t2=threading.Thread(target=f_cube,args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()


