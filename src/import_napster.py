import pandas as pd
import ApiNapster_functions as fn
import time


#Artists for requests:
    #Import only one column
field = 'artist_name'
df = pd.read_csv('../INPUT/song_info.csv', usecols=field)

    #Format the strings to introduce them in the path for the API request
artists = list(df.artist_name.unique())
artists_path= [e.lower().replace(' ','-') for e in artists]

#create a dictionary with info of all the artists availble
dictionary = {}
for e in artists_path:
    dictionary[e] = fn.artist_dict(e)
    #Hold requests at low rate to ease the server
    time.sleep(0.2)

