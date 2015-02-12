import requests
from datetime import datetime
#from bs4 import BeautifulSoup

# example artist_id: 13saZpZnCDWOI9D4IJhp1f
def fetchAlbumIds(artist_id):
    url = "https://api.spotify.com/v1/artists/" + artist_id + "/albums?market=US&album_type=album"
    info = requests.get(url)
    info = info.json()
    info = info['items']

    album_id_list = []
    for i in info:
    	album_id_list.append(i['id'])
    #print(album_id_list)
    return(album_id_list)

def fetchAlbumInfo(album_id):
    
    #the codes below find ALL RELATED albums

#    url = "https://api.spotify.com/v1/albums/" + album_id
#    req = requests.get(url)

#    req = req.json()
#    artist_id = req['artists'][0]['id']

#    artist_id_list = fetchAlbumIds(artist_id)

#    album_date_list = []
#    album_id_associated_list = []
#    album_pop_list = []
#    album_name_list = []
#    album_info_dict = {}

#    for i in artist_id_list:
#    	url = "https://api.spotify.com/v1/albums/" + i
#    	req2 = requests.get(url)
#    	req2 = req2.json()

#    	release_date = req2['release_date'] #finding the year
#    	release_date_year = release_date[:4]
#    	album_date_list.append(release_date_year)

#    	album_id_associated = req2['id']   #finding the album id
#    	album_id_associated_list.append(album_id_associated)

#    	album_pop = req2['popularity']  #finding the popularity
#    	album_pop_list.append(album_pop)

#    	album_name = req2['name']
#    	album_name_list.append(album_name)

#    album_info_dict['artist_id'] = artist_id 
#    album_info_dict['album_id'] = album_id_associated_list
#    album_info_dict['name'] = album_name_list
#    album_info_dict['year'] = album_date_list
#    album_info_dict['popularity'] = album_pop_list

#    print(album_info_dict)

	
	url = 'https://api.spotify.com/v1/albums/' + album_id
	req = requests.get(url)#print url
	if req.ok == False: print('Error in fetchAlbumInfo Request')
	req.json()
	myjson = req.json()
	artist_info = myjson.get('artists')
	get_artist_id = artist_info[0]['id']
	get_album_id = album_id
	get_name = myjson.get('name')
	get_date = myjson.get('release_date')
	get_year = get_date[0:4]
	get_popularity = myjson.get('popularity')
	keys = ['artist_id', 'album_id', 'name', 'year', 'popularity']
	values = [get_artist_id, get_album_id, get_name, get_year, get_popularity]
	album_info_dict = dict(zip(keys,values))
	return(album_info_dict)



#fetchAlbumIds('13saZpZnCDWOI9D4IJhp1f')
#fetchAlbumInfo('5Swr80WlTTC0PKExtoU4jU')