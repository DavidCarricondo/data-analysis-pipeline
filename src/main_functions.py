#Functions to bring from main
import json
import requests
import matplotlib.pyplot as plt
from src.ApiNapster_functions import cleanName
from src.wiki_scrapping import wiki_scrap

def general_report(data):
    print('You chose no band, here is a report of all the songs:');print('')
    print(f'The mean *speechiness* of a top song is {round(data.speechiness.mean(),2)} in a scale from 0 to 1')
    print(f'The mean *danceability* of a top song is {round(data.danceability.mean(),2)} in a scale from 0 to 1')
    print(f'The mean *fat_burning* of a top song is {round(data.fat_burning.mean(),2)}')
    print(data[['speechiness','danceability', 'fat_burning']].describe(include='all'))
    col = ['danceability', 'speechiness', 'fat_burning']
    for c in col:    
        plt.hist(data[c], bins=20, color='c', edgecolor='k', alpha=0.65)
        plt.title('How danceable is this song?')
        plt.xlabel(f'{c} index')
        plt.axvline(data[c].mean(), color='black', linestyle='dashed', linewidth=1)
        plt.show()

def gen_report(temp, data,band, dict, genre=False):
    print(band.upper())
    print(dict[cleanName(band)]['bio'])
    wiki_scrap(artist=cleanName(band))
    print('''
This is the most popular song of the band: 
            ''')
    print(temp[['artist_name', 'song_name','speechiness', 'danceability', 'fat_burning']][temp.song_popularity==temp.song_popularity.max()])
    print('''
This are other songs that topped from this band: 
            ''')
    top = list(temp.song_name[temp.song_popularity==temp.song_popularity.max()])
    for e in temp['song_name']: 
        if e not in top: print(e) 

    if genre == True:
        genre = temp['genre'].iloc[0]
        print(f'''
    This song belongs to the {genre.upper()} genre
        ''')
        print('''
    This are the aggregated values per music genre. Where is your song?
        ''')
        print(data[['danceability', 'speechiness', 'fat_burning', 'genre']].groupby('genre').agg(['mean', 'max', 'min']))
        data = data[data.genre==genre]
    col = ['danceability', 'speechiness', 'fat_burning']
    for c in col:    
        plt.hist(data[c], bins=20, color='c', edgecolor='k', alpha=0.65)
        plt.title('How danceable is this song?')
        plt.xlabel(f'{c} index') if genre==False else plt.xlabel(f'{c} index in {genre}')
        plt.axvline(data[c].mean(), color='black', linestyle='dashed', linewidth=1)
        plt.axvline(temp[c].mean(), color='blue', linestyle='dashed', linewidth=1)
        plt.show()
    

#Get the lyrics from a lyrics api https://lyricsovh.docs.apiary.io
def getlyric(band, song):
    url = 'https://api.lyrics.ovh/v1/'
    tail = band.replace('-', ' ')+'/'+song
    res = requests.get(url+tail)
    if res.status_code==404:
        return 'Sorry, there are no lyrics available for that song'
    else:
        lyr = json.loads(res.text)
        return lyr['lyrics']