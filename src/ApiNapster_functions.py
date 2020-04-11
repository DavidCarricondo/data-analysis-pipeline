
import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup


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
    if len(json1['artists'])==0:
        return None
    #Try the attributes that are not allways in an artist json
    try:
        bio = BeautifulSoup(json1['artists'][0]['bios'][0]['bio'], 'html.parser').text
    except:
        bio = None
    try:
        similars = getName(json1['artists'][0]['links']['contemporaries']['href'],'artists')
    except:
        similars = None
    return {'bio' : bio,
            'blurb' : json1['artists'][0]['blurbs'],
            'similars' : similars,
            'genres' : getName(json1['artists'][0]['links']['genres']['href'],'genres'),
            'images' : json1['artists'][0]['links']['images']['href']}