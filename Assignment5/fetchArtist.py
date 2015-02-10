#from bs4 import BeautifulSoup
import sys
import requests
import csv
import json

def fetchArtistId(name):
	"""Using the Spotify API search method, take a string that is the artist's name, 
    and return a Spotify artist ID.
    """
	
	name = name.replace('', '%20') # getting rid of spaces
	
	url= "https://api.spotify.com/v1/search?q=" + name + "&type=artist" #forming a readable URL
	
	req = requests.get(url)
	assert req.ok, 'No record found.'
	
	dict = req.json()
	assert dict.get('artists').get('items'), 'Artists not found.'
	
	id = dict['artists']['items'][0]['uri'] # can also index 'id'
	id = id.split(':')[2]
	
	#print(id)
	return(id)
	

# example id: 0IEXBEvkiRDvASHhB1va4z
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
    
    
    
    
    


#fetchArtist(sys.argv[1])
#fetchArtistInfo(sys.argv[1])
