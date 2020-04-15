import pandas as pd
import matplotlib.pyplot as plt
from argparse import ArgumentParser
import sys, os, glob, json, requests
import src.main_functions as fn


parser = ArgumentParser(description="This program returns a small report of the top song of your favorite band,\
\measuring the speechiness, the danceability and an index to measure how good is this song for burning calories dancing to it :)")

parser.add_argument("--band",help="which band to look for", default=None)
parser.add_argument("--bygenre", type=bool,  help="Do you want to analyze it comparing it to its genre? yes/no", default= 'no')
parser.add_argument("--pdf", type=bool, help="Do you want to generate a pdf from the report? yes/no", default= 'no')

args = parser.parse_args()

### Data:   
data = pd.read_csv('OUTPUT/data.csv')
# read file
with open('OUTPUT/artists_json.json', 'r') as myfile:
    string=myfile.read()
string_json = json.loads(string)
dict_json = json.loads(string_json)

if __name__=='__main__':
    fn.main_function(data=data, dict_json=dict_json, band=args.band, bygenre=args.bygenre, pdf=args.pdf) 
