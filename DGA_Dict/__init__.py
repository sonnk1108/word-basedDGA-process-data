import os
import pandas as pd
import wordninja as nj
path="Wd"
str=""
wd=pd.DataFrame()
for filename in os.listdir(path):
    if (filename.endswith('.txt')):
        df=pd.read_csv(os.path.join(path,filename),header=None)
        wd=pd.concat([wd,df])

wd=wd.drop_duplicates()
dict_=[]
st=""
for i in wd.values:
    try:
        z=nj.split(i[0])
        for w in z:
            st=st+w+"\n"
    except:
        pass


f=open('dict_.txt','a')
f.write(st)
