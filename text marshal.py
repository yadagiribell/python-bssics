import  marshal
fp=open("marshal.txt","rb")
data=marshal.load(fp)

exec(data)
