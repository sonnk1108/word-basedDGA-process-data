import os
import pandas as pd
label=0
path= r"Backup/Extract_data"

all_dga=pd.DataFrame()
for filename in os.listdir(path):
    if(filename.endswith('.csv') ):
        df = pd.read_csv(os.path.join(path, filename))
        if df.shape[0] >8000:
            label=label+1
            print("reset label of dataset {} label {} ".format(filename,label))
            df = pd.read_csv(os.path.join(path, filename))
            df['label']=label
            df=df.drop_duplicates()
            print(df.shape[0])
            all_dga=pd.concat([all_dga,df.head(10000)])
all_dga.to_csv("Extract_data/final.csv")
