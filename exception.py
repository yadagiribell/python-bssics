a=int(input("enter a value"))
#b=int(input("enter b value"))
try:
   # c=a/b
    #print("value of c",c)
    x=[1,2,3,4,5]
    print(x[5])
except NameError:
   #print("cant divide by zero")
    print("b value is not mention,")
except ZeroDivisionError:
    print("arithematic exception")
except ValueError:
    print("Value error")
except IndexError:
    print("Array index out of bounds")
except KeyError:
    print("key value error")
