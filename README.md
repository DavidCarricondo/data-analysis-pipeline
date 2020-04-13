# pipeline-project: Dancing to your band


<p>&nbsp;&nbsp;&nbsp;&nbsp;Ironhack project on data pipelines that uses a kaggle data set enriched with data from two different APIS (with and without APIKEY) and from wikipedia scrapping.

### Objective and info

<p>&nbsp;&nbsp;&nbsp;&nbsp;The program will return the bio of your chosen band together with an image, the top song of the band, some stats of the song, statistics on the different genres, plots and lyrics to the song.

<p>&nbsp;&nbsp;&nbsp;&nbsp;The program takes three optional arguments. First one is <strong>band</strong>, which is the name of the band (works mostly for US and other international bands). If the argument is not supply, the program return a simple report with the stats of all the songs. The second argument is <strong>bygenre</strong> which takes a yes or no, and groups the data in genres and returns statistic on each one. Third argument is <strong>pdf</strong> that also takes yes or no and generates a pdf with the reported info.<p>&nbsp;&nbsp;&nbsp;&nbsp; <strong>Danceability</strong> is a measure of how easily you can dance to the song (head banging is not considered dancing here :P ). <strong>Speechiness</strong> is a measure of the wordiness of the lyrics, and <strong>fat_burning</strong> is a variable created from a formula that convines the lenght of the song, how energetic it is, and how danceable it is. From 0 to 100 (although it can be higher for extremely long, danceable and energetic songs), how good is this song for burning those fats!

### Flow

&nbsp;&nbsp;&nbsp;&nbsp;There is a preprocess done by `cleaning_db.py` that imports bios and other data from the Napster API through `import_napster.py` and `ApiNapster_functons.py`(about 22000 requestes, more than three hours sending requests to the API :) )</p> During the call to the program there are two more live requests, for the lyrics, to to the API from *lyrics.ovh*, and for the image, via web scrapping in *wikipedia.org*. A pdf is generated from the funcion in `generate_pdf.py` and it is authomatically opened with `xdg-open *.pdf`. 

### Examples

&nbsp;&nbsp;&nbsp;&nbsp; You might want to try some examples like:
<p>`python3 --band Pearl Jam --bygenre yes --pdf true`</p>
<p>`python3 --band the 'rolling stones' --bygenre no --pdf true`</p>
<p>`python3 --band 'eric clapton'`</p>

## Rock on!
