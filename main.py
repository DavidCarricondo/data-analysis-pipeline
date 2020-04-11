import random
import os 
import sys
from argparse import ArgumentParser
import subprocess

## BY default, the program should return a report with the means and distribution of some parameters of the whole song dataset and divide by genres
# With a band name, it will produce a report with a comparision of the most popular song by that group compared to the rest of the songs 
#  and to the genres summary. It also produces a bio of the band and other similar bands
#THe lyric argument shows the lyric of the song if available in the specific API
#The picture argument returns a picture of a band retrieved from web scrapping.

def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])
    #return proc.stdout.read()

def my_group(lang,lugar):
    pass


parser = ArgumentParser(description="This program returns a report of the top song of your favorite band")

parser.add_argument("--band",help="el idioma con el que saludar", default="es")
parser.add_argument("--lyric",help="desde donde saludar", default="la playa")
parser.add_argument("--picture",help="veces que saludar", default=1, type=int)

args = parser.parse_args()
#print(args)
