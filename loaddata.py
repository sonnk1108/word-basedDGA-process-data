import os
import pandas as pd
import extract_data as ex
import  time
label=0
l=0
path= "Data"

for filename in os.listdir(path):
    if(filename.endswith('.csv')   and 'banjori' in filename):
        print('extrating data for {} {}'.format(filename,label))


        st=time.time()
        df=pd.read_csv(os.path.join(path,filename))

        #try:
          #  df=df.drop(columns=['Unnamed: 0'],axis=1)
        #except:
        #    df=df.drop(columns=0,axis=1)
       # df.columns = ['Domain']
       # df['label']=2
        df['type']='banjori'
        df['Domain_cut']=df['1'].apply(lambda x: x.split('.')[0].strip().lower() )
        cols = [ 'Length', 'asii_value', 'word_count', 'Vowel_Count', 'consonants', 'syllable_count',
                'underscore', 'hyphen', 'countdi','tandi', 'tanv', 'count_n', 'count_v', 'count_adj', 'max_length_word',
                'min_length_word', 'ratito_char','word_dga','ratio_dga','label','type']

        data_extract=[]
        for i in df.values:
            if(len(i[2])>=3):
                print(i[0],i[1],i[2])
                data_extracting=ex.generateDataset(i[2],1)+[i[1]]
                data_extract.append(data_extracting)
        final_dataset=pd.DataFrame(data_extract,columns=cols)
        #final_dataset.drop_duplicates()
        final_dataset.to_csv('Extract_data/wb{}'.format(filename),index=False)
        print(df.shape)
        print("extract data for {} successfull taking  {} s ".format(filename,time.time()-st))
        label = label + 1
