#from bs4 import BeautifulSoup
import sys
import requests
import csv
import json

def fetchArtistId(name):
	url= "https://api.spotify.com/v1/search?q=" + name + "&type=artist"
	req = requests.get(url)
	#req = req[0].json()
	print(req)
	print(type(req))

def fetchArtistInfo(artist_id):
    """Using the Spotify API, takes a string representing the id and
`   returns a dictionary including the keys 'followers', 'genres', 
    'id', 'name', and 'popularity'.
    """
    pass


fetchArtistId(sys.argv[1])
