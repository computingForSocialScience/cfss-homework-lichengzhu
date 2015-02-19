#from bs4 import BeautifulSoup
import sys
import requests
import csv
import json

def fetchArtistId(name):
	"""Using the Spotify API search method, take a string that is the artist's name, 
    and return a Spotify artist ID.
    """
	
	#underline_name = name.replace('', '%20') # getting rid of spaces
	
	url= "https://api.spotify.com/v1/search?q=" + name + "&type=artist" #forming a readable URL
	print(url)
	
	req = requests.get(url)
	assert req.ok, 'No record found.'
	
	dict = req.json()
	
	id = dict['artists']['items'][0]['id'] # can also index 'uri'

	
	#print(id)
	return(id)
	

# example id: 13saZpZnCDWOI9D4IJhp1f
def fetchArtistInfo(artist_id):
    url = "https://api.spotify.com/v1/artists/" + artist_id
    
    req = requests.get(url)
    assert req.ok, 'No record found.'
    
    dict = req.json()
    assert dict.get('name'), 'Artists not found.'
    
    info_dict = {}
    info_dict['followers'] = dict['followers']['total']
    info_dict['genres'] = dict['genres']
    info_dict['id'] = dict['id']
    info_dict['name'] = dict['name']
    info_dict['popularity'] = dict['popularity']
    
    #print(info_dict)
    return(info_dict)
    
    
    
    
    


#fetchArtistId('Lily Allen')
#fetchArtistInfo('13saZpZnCDWOI9D4IJhp1f')
