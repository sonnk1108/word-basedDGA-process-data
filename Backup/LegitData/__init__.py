import pandas as pd
import  extract_data as ex
df=pd.read_csv("https://raw.githubusercontent.com/andrewaeva/DGA/master/all_legit.txt",sep=" ",header=None)
df.columns=['Domain','Label']
df['Domain_cut']=df['Domain'].apply(lambda x: x.split('.')[0].strip().lower() )
cols=['Domain','Length','asii_value','word_count','Vowel_Count','consonants','syllable_count','underscore','hyphen','tandi','tanv','count_n','count_v','count_adj','max_length_word','min_length_word','ratito_char','label']
data_extract=[]
for i in df.head(200000).values:
    print(i[0])
    data_extracting = ex.generateDataset(i[0], i[2], i[1])
    data_extract.append(data_extracting)
final_dataset = pd.DataFrame(data_extract, columns=cols)
final_dataset.to_csv('{}'.format("legitdata.csv"))