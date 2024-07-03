import pickle
fp=open("picklefile.txt","wb")
cn=["dhoni","virat","dhawan"]
pickle.dump(cn,fp)
fp.close()