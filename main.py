import pandas as pd
import matplotlib.pyplot as plt
from argparse import ArgumentParser
import sys, os, glob, json, requests
import src.main_functions as fn
from src.ApiNapster_functions import cleanName
from src.generate_pdf import create_pdf

parser = ArgumentParser(description="This program returns a small report of the top song of your favorite band,\
\measuring the speechiness, the danceability and an index to measure how good is this song for burning calories dancing to it :)")

parser.add_argument("--band",help="which band to look for", default=None)
parser.add_argument("--bygenre", help="Do you want to analyze it comparing it to its genre? yes/no", default= 'no')
parser.add_argument("--pdf", help="Do you want to generate a pdf from the report? yes/no", default= 'no')

band= (sys.argv[2] if len(sys.argv)>1 else None)
bygenre=(sys.argv[4] if len(sys.argv)>3 else 'no')
pdf=(sys.argv[6] if len(sys.argv)>5 else 'no')
    
args = parser.parse_args()

### Data:   
data = pd.read_csv('OUTPUT/data.csv')
# read file
with open('OUTPUT/artists_json.json', 'r') as myfile:
    string=myfile.read()
string_json = json.loads(string)
dict_json = json.loads(string_json)

fn.main_function(data=data, dict_json=dict_json, band=band, bygenre=bygenre, pdf=pdf) 
