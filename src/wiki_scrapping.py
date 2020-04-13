import requests
from bs4 import BeautifulSoup
import urllib.request
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def wiki_scrap(artist):
#Scrapping the wikipedia site of the artist
    url='https://wikipedia.org/wiki/'
    art= artist.replace('-','_')
    res = requests.get(url+art)
    soup = BeautifulSoup(res.text, features='html.parser')
    src = soup.select('.image img')[0]['src']

    #show image
    urlpic = 'https:'+src
    urllib.request.urlretrieve(urlpic, 'temp.jpg')
    img=mpimg.imread('temp.jpg')
    imgplot = plt.imshow(img)
    plt.show()
    os.remove('temp.jpg')