
import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

#Function to prepare the names as paths:
cleanName= lambda e: e.lower().replace(' ','-').replace('.','').replace('&','and')\
               .replace('é','e').replace('ø','o').replace('\'','').replace('!','')\
                   .replace('*','').replace('$','s')

#Prepare APIKEY:
load_dotenv()
    # Load the apikey
apiKey = os.getenv("API_NAPSTER")

#Function to automate the requests:
def getFromNapster(art_path=None, url='', apiKey=apiKey):
    if art_path:
        # Construct the resource url
        url = f"https://api.napster.com/v2.2/artists/{art_path}"
    else: url=url
    # If apiKey is defined, pass a header
    headers = {"apikey":f"{apiKey}"} if apiKey else {}
    # Perform the request
    res = requests.get(url, headers=headers)
    # Extract json from body response
    return res.json()


#Function to get subrequests from the main request. Type must be 'artists' to get similar artists or 'genres' to get the genres
def getName(url, type):
    new_json = getFromNapster(url=url)
    return [x['name'] for x in new_json[type]]

#Funcion that uses the other functions to create an artist dictionary with info
def artist_dict(artist):
    json1 = getFromNapster(artist)
    #Some artists with non valid characters may be skipped
    if 'artists' in json1:
        if len(json1['artists'])==0:
            return None
    else: return None
    #Try the attributes in case they are not in the artist json
    if 'bios' in json1['artists'][0]:
        bio = BeautifulSoup(json1['artists'][0]['bios'][0]['bio'], 'html.parser').text
    else:    bio = None
    if 'blurbs' in json1['artists'][0]:
        blurb = json1['artists'][0]['blurbs']
    else: blurb = None
    if 'contemporaries' in json1['artists'][0]['links']:
        similars = getName(json1['artists'][0]['links']['contemporaries']['href'],'artists')
    else: similars = None
    if 'genres' in json1['artists'][0]['links']:
        genres = getName(json1['artists'][0]['links']['genres']['href'],'genres')
    else:   genres = None
    if 'images' in json1['artists'][0]['links']:
        images= json1['artists'][0]['links']['images']['href']
    else:   images = None
    return {'bio' : bio,
            'blurb' : blurb,
            'similars' : similars,
            'genres' : genres,
            'images' : images}