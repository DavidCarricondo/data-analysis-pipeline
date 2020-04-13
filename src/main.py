import pandas as pd
import json
import matplotlib.pyplot as plt
import requests
from argparse import ArgumentParser
import sys
import main_functions as fn
from ApiNapster_functions import cleanName

parser = ArgumentParser(description="This program returns a report of the top song of your favorite band or the song of your choosing that has been on top")

parser.add_argument("--band",help="which band to look for", default=None)
parser.add_argument("--bygenre", help="Do you want to analyze it by genre? yes/no", default= 'no')

try:
    band=sys.argv[2]
except: band=None
try:
    bygenre=sys.argv[4]
except: bygenre = 'no'
    

args = parser.parse_args()

### Data:   
data = pd.read_csv('../OUTPUT/data.csv')
# read file
with open('../OUTPUT/artists_json.json', 'r') as myfile:
    string=myfile.read()
string_json = json.loads(string)
dict_json = json.loads(string_json)


if band==None:
    fn.general_report(data=data)
else:
    if bygenre=='yes':
        if len(data[data.artists_path==cleanName(band)])==0:
            print("Sorry, I don't seem to find that band :(")
        else:
            temp = data[data.artists_path==cleanName(band)]
            print(fn.gen_report(temp=temp, data=data,band=band,dict=dict_json, genre=True))   

            lyric = ''
            while lyric not in ['y', 'n']:
                lyric = input('Do you want to see the lyrics of the song?(y/n): ')
            if lyric == 'y':
                top = list(temp.song_name[temp.song_popularity==temp.song_popularity.max()])
                song = top[0].lower().split('-')[0].strip()
                print(fn.getlyric(band, song))

    else:
        if len(data[data.artists_path==cleanName(band)])==0:
            print("Sorry, I don't seem to find that band :(")
        else:
            temp = data[data.artists_path==cleanName(band)]
            print(fn.gen_report(temp=temp, data=data,band=band,dict=dict_json, genre=False))

            lyric = ''
            while lyric not in ['y', 'n']:
                lyric = input('Do you want to see the lyrics of the song?(y/n): ')
            if lyric == 'y':
                top = list(temp.song_name[temp.song_popularity==temp.song_popularity.max()])
                song = top[0].lower().split('-')[0].strip()
                print(fn.getlyric(band, song))

