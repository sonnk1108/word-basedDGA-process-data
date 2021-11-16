import pandas  as pd
import wordninja as ninja
import time
import re
dict_dga=pd.read_csv('DGA_Dict/word_dga_dict.csv')
List_dga=list(dict_dga['0'])
dict_ = pd.read_csv('word_dict_common_use.csv',sep=';')
dict_noun=dict_['word'][dict_['Value']=='noun']
dict_verd=dict_['word'][dict_['Value']=='verb']
dict_adj=dict_['word'][dict_['Value']=='adjective']
#data_legit = pd.read_csv('https://raw.githubusercontent.com/andrewaeva/DGA/master/all_legit.txt',delim_whitespace=True)
#data_dga=pd.read_csv("Gozi/gozy_dga.csv")
#data_dga=data_dga.drop(columns='Unnamed: 0',axis=1)
#print(data_dga)

#data_legit.columns=['Domain','Label']
#data_legit['Domain_cut']=data_legit['Domain'].apply(lambda x: x.split('.')[0].strip().lower() )
#print(data_dga['Domain'])
#data_dga['Domain_cut']=data_dga['Domain'].apply(lambda x: x.split('.')[0].strip().lower() )

#dataset=pd.concat([data_dga])

def countwordDGA(word):
    list_ = ninja.split(word)
    count_word_dga=0
    for i in list_:
        if(i in List_dga):
            count_word_dga=count_word_dga+1
    return count_word_dga
def countWordinDict(word):
    list_ = ninja.split(word)
    count_n = 0  # count number of word in dict noun, dict verb, and dict adj
    count_v = 0
    count_adj = 0
    for i in list_:
        if (i in dict_noun.array):
            count_n = count_n + 1
        if (i in dict_verd.array):
            count_v = count_v + 1
        if (i in dict_adj.array):
            count_adj = count_adj + 1
    return count_n, count_v, count_adj


def count_syllables(word):
    return len(
        re.findall('(?!e$)[aeiouy]+', word, re.I) +
        re.findall('^[^aeiouy]*e$', word, re.I)
    )


def sum_ascii(word):
    total = 0
    for i in word:
        total = total + ord(i)
    return total


# this function use to count vovew, consutnant...
def ratioLenofWord(word):
    list_ = ninja.split(word)
    count = 0
    for i in list_:
        if i in dict_:
            count = count + len(i)
    return count


def extractFeature(word):
    consonants = 0  # number of consonant
    vowels = 0  # number of vowels
    underscore = 0  # do the word has character _ ?
    hyphen = 0  # do the word has character - ?
    count_n = 0  # count number of word in dict noun, dict verb, and dict adj
    count_v = 0
    count_adj = 0
    tandi = 0
    for i in word:
        if (i == '_'):
            underscore = 1
        if (i in '-123456789'):
            hyphen = 1
            tandi = tandi + 1
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or
                i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            vowels = vowels + 1;  # vowel counter is incremented by 1
        else:
            consonants = consonants + 1;

        count_n, count_v, count_adj = countWordinDict(word)
    return vowels, consonants, underscore, hyphen, count_n, count_v, count_adj, tandi


# this function use to extract data for a domain and return it in array
def generateDataset( word,label):
    # tanv the vowel distribution the domain name d = vowels/length
    # consonants number of consonant
    # vowels number of vowels
    # underscore  do the word has character _ ?
    # hyphen  do the word has character - ?
    # tandi is ratio between character - and length(word)

    asii_value = sum_ascii(word)
    Length = len(word)
    word_count = len(ninja.split(word))
    Vowel_Count, consonants, underscore, hyphen, count_n, count_v, count_adj, tan = extractFeature(word)
    tanv = Vowel_Count / Length
    max_length_word = max(len(w) for w in ninja.split(word))
    min_length_word = min(len(w) for w in ninja.split(word))
    syllable_count = count_syllables(word)
    ratito_char = ratioLenofWord(word) / Length
    coundi=tan
    tandi = tan / Length
    group_lenght=group_length(Length)
    word_dga=countwordDGA(word)
    ratio_dga=word_dga/word_count
   # print('domain {} '.format(domain))

    return [Length,asii_value, word_count, Vowel_Count, consonants, syllable_count, hyphen, coundi,tandi,tanv, count_n,
            count_v, count_adj, max_length_word, min_length_word, ratito_char,group_lenght,word_dga,ratio_dga,label]

def group_length(x):
  k=x
  if(k>=1 and k <= 8):
    return 1
  elif (k > 8 and k <=12):
    return 2
  elif (k >12 and k <= 14):
    return 3
  elif (k>14):
    return 4
  else:
    return 0
cols=['Domain','Length','asii_value','word_count','Vowel_Count','consonants','syllable_count','underscore','hyphen','tandi','tanv','count_n','count_v','count_adj','max_length_word','min_length_word','ratito_char','label']
#data=dataset.values
#data_extract=[]
#st=time.time()
# data_extracting=generateDataset(i[0],i[2],i[1])
 # print(data_extracting)
 # data_extract.append(data_extracting)
#end=time.time()
#final_dataset=pd.DataFrame(data_extract,columns=cols)
