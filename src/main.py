import pandas as pd
import matplotlib.pyplot as plt
from argparse import ArgumentParser
from ApiNapster_functions import cleanName


## BY default, the program should return a report with the means and distribution of some parameters of the whole song dataset and divide by genres
# With a band name, it will produce a report with a comparision of the most popular song by that group compared to the rest of the songs 
#  and to the genres summary. It also produces a bio of the band and other similar bands
#THe lyric argument shows the lyric of the song if available in the specific API
#The picture argument returns a picture of a band retrieved from web scrapping.

data = pd.read_csv('../OUTPUT/data.csv')
def my_group(band=None, song='top', lyric='no', picture='no'):
    if band==None:
        print('You chose no band, here is a report of all the songs:')
        print(f'The mean *speechiness* of a top song is {round(data.speechiness.mean(),2)} in a scale from 0 to 1')
        print(f'The mean *danceability* of a top song is {round(data.danceability.mean(),2)} in a scale from 0 to 1')
        print(f'The mean *fat_buring* of a top song is {round(data.fat_burning.mean(),2)}')





parser = ArgumentParser(description="This program returns a report of the top song of your favorite band or the song of your choosing that has been on top")

parser.add_argument("--band",help="which band to look for", default="es")
parser.add_argument("--song", help="which song to analyze", default= 'top')
parser.add_argument("--lyric",help="do you want to look for the lyrics of the song?", default="no")
parser.add_argument("--picture",help="do you want to see a picture of the band", default='no')

args = parser.parse_args()
#print(args)

my_group()