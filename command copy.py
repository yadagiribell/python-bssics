from sys import argv
if len(argv)==3:

    try:
        fp1=open(argv[1],"r")
        fp2=open(argv[2],"w+")
        for i in fp1:
            fp2.write(i)
        print("file is copied succesfully")
        fp2.seek(0,0)
        cont=fp2.read()
        print(cont)
        fp1.close()
        fp2.close()






    except Exception:
        print("error in copying file")