import pandas as pd

df_song = pd.read_csv('../INPUT/song_data.csv')
df_song_inf = pd.read_csv('../INPUT/song_info.csv') 

#Remove duplicated songs (same song in different albums) from both datasets
df_song = df_song.drop_duplicates(['song_name'])
df_song_inf = df_song_inf.drop_duplicates(subset=['song_name','artist_name'])

#merge both datasets:
data = pd.merge(df_song,df_song_inf,on='song_name')

#Inport from API napster:


#Export data
data.to_csv("../OUTPUT/data.csv")