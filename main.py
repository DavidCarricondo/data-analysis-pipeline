import pandas as pd
import matplotlib.pyplot as plt
from argparse import ArgumentParser
import sys, os, glob, json, requests
import src.main_functions as fn
from src.ApiNapster_functions import cleanName
from src.generate_pdf import create_pdf

parser = ArgumentParser(description="This program returns a report of the top song of your favorite band or the song of your choosing that has been on top")

parser.add_argument("--band",help="which band to look for", default=None)
parser.add_argument("--bygenre", help="Do you want to analyze it by genre? yes/no", default= 'no')
parser.add_argument("--pdf", help="Do you want to analyze it by genre? yes/no", default= 'no')

try:
    band=sys.argv[2]
except: band=None
try:
    bygenre=sys.argv[4]
except: bygenre = 'no'
try:
    pdf=sys.argv[6]
except: pdf = 'no'
    
args = parser.parse_args()

### Data:   
data = pd.read_csv('OUTPUT/data.csv')
# read file
with open('OUTPUT/artists_json.json', 'r') as myfile:
    string=myfile.read()
string_json = json.loads(string)
dict_json = json.loads(string_json)

fn.main_function(data=data, dict_json=dict_json, band=band, bygenre=bygenre, pdf=pdf) 
