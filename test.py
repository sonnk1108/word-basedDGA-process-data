import pandas  as pd
import wordninja as ninja
import time
import re
df=pd.read_csv('Backup/Data/TEST_ex5.csv')
df2=pd.read_csv('Extract_data/wbTEST_ex5.csv')
df3=pd.concat([df,df2],axis=1)
print(df3)