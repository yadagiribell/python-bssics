fp1=open("csea.txt","r")
if fp1:
    print("file is open succesfully")
print(list(fp1))
content=fp1.read()
print(content)
