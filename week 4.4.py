def invert_content(dic):
    n=int(input("enter no of values"))
    dic={ }
    for i in range(n):
     keys=input("enter key")
     value=input("enter value")
      dic[keys]=value
       print(dic)
       print("after invertion")
print(invert_content(dic))
