import pandas as pd
path='https://data.netlab.360.com/feeds/dga/ranbyus.txt'
df=pd.read_csv(path,skiprows=20,sep='\t',header=None)
df['Domain']=df[0]
df['Domain'].head(10000).to_csv(r'C:\Users\Tranl\PycharmProjects\Detect_DGAbotnet\Raw_data/ranbyus.csv')
