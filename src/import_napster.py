import requests
import os
from dotenv import load_dotenv


#Prepare APIKEY:
load_dotenv()
    # Load the apikey
apiKey = os.getenv("API_NAPSTER")
