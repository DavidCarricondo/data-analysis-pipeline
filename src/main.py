import pandas as pd
import json
import matplotlib.pyplot as plt
import requests
from argparse import ArgumentParser
import sys
from ApiNapster_functions import cleanName

parser = ArgumentParser(description="This program returns a report of the top song of your favorite band or the song of your choosing that has been on top")

parser.add_argument("--band",help="which band to look for", default=None)
parser.add_argument("--song", help="which song to analyze", default= 'top')
parser.add_argument("--bygenre", help="which song to analyze", default= False, type=bool)
parser.add_argument("--picture",help="do you want to see a picture of the band", default='no')
band=sys.argv[2]

args = parser.parse_args()

### Data:
data = pd.read_csv('../OUTPUT/data.csv')
# read file
with open('../OUTPUT/artists_json.json', 'r') as myfile:
    string=myfile.read()
string_json = json.loads(string)
dict_json = json.loads(string_json)


if band==None:
    print('You chose no band, here is a report of all the songs:');print('')
    print(f'The mean *speechiness* of a top song is {round(data.speechiness.mean(),2)} in a scale from 0 to 1')
    print(f'The mean *danceability* of a top song is {round(data.danceability.mean(),2)} in a scale from 0 to 1')
    print(f'The mean *fat_burning* of a top song is {round(data.fat_burning.mean(),2)}')
    print(data[['speechiness','danceability', 'fat_burning']].describe(include='all'))
    plt.hist(data.danceability, bins=20, color='c', edgecolor='k', alpha=0.65)
    plt.axvline(data.danceability.mean(), color='k', linestyle='dashed', linewidth=1)
    plt.show()
else:
    if len(data[data.artists_path==cleanName(band)])==0:
        print("Sorry, I don't seem to find that band :(")
    else:
        temp = data[data.artists_path==cleanName(band)]
        print(band.upper())
        print(dict_json[cleanName(band)]['bio'])
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

        lyric = ''
        while lyric not in ['y', 'n']:
            lyric = input('Do you want to see the lyrics of the song?(y/n): ')
        if lyric == 'y':
            url = 'https://api.lyrics.ovh/v1/'
            tail = band.replace('-', ' ')+'/'+top[0].lower()
            res = requests.get(url+tail)
            lyr = json.loads(res.text)
            print(lyr['lyrics'])