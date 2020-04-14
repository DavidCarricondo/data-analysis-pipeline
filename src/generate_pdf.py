# importing libraries
from fpdf import FPDF
import requests, json
import pandas as pd
from subprocess import Popen


def create_pdf(band, data, dict):
    band=band.lower().replace(' ','-').replace('.','').replace('&','and').replace('é','e').replace('ø','o').replace('\'','').replace('!','')\
                   .replace('*','').replace('$','s')
    temp = data[data.artists_path==band]
    agg = data[['danceability', 'speechiness', 'fat_burning', 'genre']].groupby('genre').agg(['mean', 'max', 'min'])
    pdf = FPDF("P","mm","A4")
    pdf.add_page()

    # Title cell:
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0,10,band.upper(),1,1,"C")

    # Band image
    pdf.set_xy(50,25)
    pdf.image("OUTPUT/temp.jpg", x = None, y = None, w = 0, h = 0)

    # Bio cells
    pdf.set_xy(10,pdf.get_y()+10)
    pdf.set_font("Times", "I", 9)
    pdf.multi_cell(0,10,dict[band]['bio'],align= 'C', border=0, fill=False)

    # Top song cell
    song = list(temp.song_name[temp.song_popularity==temp.song_popularity.max()])[0]
    danceability = round(list(temp.danceability[temp.song_popularity==temp.song_popularity.max()])[0],2)
    speechiness = round(list(temp.speechiness[temp.song_popularity==temp.song_popularity.max()])[0],2)
    fat_burning = round(list(temp.fat_burning[temp.song_popularity==temp.song_popularity.max()])[0],2)

    pdf.set_xy(50,pdf.get_y()+5)
    pdf.set_font("Times", "B", 10)
    pdf.cell(0,8,f'The most popular song of {band} is "{str(song)}"',0,1,"L")
    pdf.set_x(50)
    pdf.cell(0,8,f'The danceability of the top songs of this band is {danceability}',0,1,"L")
    pdf.set_x(50)
    pdf.cell(0,8,f'A speechiness of {speechiness}',0,1,"L")
    pdf.set_x(50)
    pdf.cell(0,8,f'And the fat-burning indes is {fat_burning}',0,1,"L")  

    pdf.add_page()

    #Creating the table:
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0,10,'Numbers by genres',0,1,"C")

    A4_width, l_margin, r_margin = 210, 10, 10
    useful_page_width = A4_width-l_margin-r_margin
    cell_width_head = useful_page_width/4
    
    pdf.cell(cell_width_head/2,8,'',1,0,'C')
    for e in {a for a,b in agg.columns}:
        pdf.cell(cell_width_head,8,e.upper(),1,0,'C')
    pdf.ln()
    pdf.cell(cell_width_head/2,8,'',1,0,'C')
    cols = ['mean', 'max', 'min']
    for i in range(3):
        for e in cols:
            pdf.cell(cell_width_head/3,8,e,1,0,'C')
    pdf.ln()
    for e,r in agg.iterrows():
        pdf.set_font("Times", "B", 9)
        pdf.cell(cell_width_head/2,8,e,1,0,'C')
        pdf.set_font("Times", "", 9)
        for i in r:
            pdf.cell(cell_width_head/3,8,str(round(i,2)),1,0,'C')
        pdf.ln()

    #Plots:
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0,10,'Plots',0,1,"C")
    pdf.image("OUTPUT/danceability.png", x = 5, y = 140, w = 90, h = 90)
    pdf.image("OUTPUT/speechiness.png", x = 110, y = 140, w = 90, h = 90)
    pdf.add_page()
    pdf.image("OUTPUT/fat_burning.png", x = 55, y = None, w = 90, h = 90)

    #Top song lyric:
    pdf.set_y(pdf.get_y()+5)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0,10,'Lyrics',0,1,"C")
    pdf.set_font("Arial", "", 9)
    song = song.lower().split('-')[0].strip()
    url = 'https://api.lyrics.ovh/v1/'+ band.replace('-', ' ')+'/'+song
    res = requests.get(url)
    lyr = json.loads(res.text)
    pdf.multi_cell(0,5,lyr['lyrics'],align= 'C', border=0, fill=False)

    pdf.output(f"OUTPUT/{band}.pdf","F")
    Popen(['/bin/bash', '-c', f'xdg-open OUTPUT/{band}.pdf'])