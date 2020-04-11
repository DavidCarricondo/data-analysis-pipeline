import pandas as pd
import ApiNapster_functions as fn
import time
import json


#Artists for requests:
    #Import only one column
field = ['artist_name']
df = pd.read_csv('../INPUT/song_info.csv', usecols=field)

    #Format the strings to introduce them in the path for the API request
artists = list(df.artist_name.unique())
artists_path= [e.lower().replace(' ','-').replace('.','').replace('&','and')\
               .replace('é','e').replace('ø','o').replace('\'','').replace('!','')\
                   .replace('*','').replace('$','s') for e in artists]
artists_path = sorted(artists_path)

#create a dictionary with info of all the artists availble
dictionary = {}
for e in artists_path:
    dictionary[e] = fn.artist_dict(e)
    print(e)
    #Hold requests at low rate to ease the server
    time.sleep(0.2)

#Convert the dictionary into a JSON
json_dictionary = json.dumps(dictionary)
#Saving it into a json file
with open('../OUTPUT/artists_json.json', 'w') as file:
    json.dump(json_dictionary, file)