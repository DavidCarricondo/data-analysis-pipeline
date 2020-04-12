import pandas as pd
import json
from ApiNapster_functions import cleanName

df_song = pd.read_csv('../INPUT/song_data.csv')
df_song_inf = pd.read_csv('../INPUT/song_info.csv') 

#Remove duplicated songs (same song in different albums) from both datasets
df_song = df_song.drop_duplicates(['song_name'])
df_song_inf = df_song_inf.drop_duplicates(subset=['song_name','artist_name'])

#merge both datasets:
data = pd.merge(df_song,df_song_inf,on='song_name')

#Create a new column with valid artists paths: (para función)
data['artists_path']= data.artist_name.apply(cleanName)
                   
#Getting results from import_napster:

# read file
with open('OUTPUT/artists_json.json', 'r') as myfile:
    string=myfile.read()

# parse file
string_json = json.loads(string)
dict_json = json.loads(string_json)

#reclassifying the genres to reduce them to 10 categories (para función)
gen = ['metal', 'alternative', 'reggaeton', 'hip-hop', 'electronic','country', 'rock', 'pop', 'blues', 'jazz']
art_genre=[]
for k in dict_json.keys():
    if (dict_json[k] == None) :
        art_genre.append((k,None))
    else:
        if dict_json[k]['genres'] == None:
          art_genre.append((k,None))
        else:
            track=0
            for g in gen:
                if any([g in x.lower() for x in  dict_json[k]['genres']]):
                    art_genre.append((k,g))
                    track+=1
                    break
            if track==0: art_genre.append((k,'undefined'))

#Adding the genres to the dataset
genres = []
for e in data['artists_path']:
    for a,g in art_genre:
        if e==a:
            genres.append(g)
            break

data['genre'] = genres


#Export data
data.to_csv("../OUTPUT/data.csv")