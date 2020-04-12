#Functions to bring from main
import json
import requests
import matplotlib.pyplot as plt
from ApiNapster_functions import cleanName


def gen_report(temp, data,band, dict, genre=False):
    print(band.upper())
    print(dict[cleanName(band)]['bio'])
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
    plt.hist(data.danceability, bins=20, color='c', edgecolor='k', alpha=0.65)
    plt.title('How danceable is this song?')
    plt.axvline(data.danceability.mean(), color='black', linestyle='dashed', linewidth=1)
    plt.axvline(temp.danceability.mean(), color='blue', linestyle='dashed', linewidth=1)
    plt.show()
    plt.close()
    plt.hist(data.speechiness, bins=20, color='c', edgecolor='k', alpha=0.65)
    plt.title('How wordy is this song?')
    plt.axvline(data.speechiness.mean(), color='black', linestyle='dashed', linewidth=1)
    plt.axvline(temp.speechiness.mean(), color='blue', linestyle='dashed', linewidth=1)
    plt.show()
    plt.hist(data.fat_burning, bins=20, color='c', edgecolor='k', alpha=0.65)
    plt.xlim(0,150)
    plt.title('Can you burn those fats dancing to this song?')
    plt.axvline(data.fat_burning.mean(), color='black', linestyle='dashed', linewidth=1)
    plt.axvline(temp.fat_burning.mean(), color='blue', linestyle='dashed', linewidth=1)
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