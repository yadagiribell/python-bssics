a=10
b=0
try:
    print(a/b)
except Exception as e:
    print("cant divide by zero", e)
finally:
    print("resource closed")