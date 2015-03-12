import sys
import networkx as nx
import pandas as pd
import random
from io import open
from artistNetworks import getEdgeList
from analyzeNetworks import randomCentralNode, combineEdgeLists, pandasToNetworkX
from fetchArtist import *
from fetchAlbums import * 

if  __name__ == '__main__': 
	artist_names = sys.argv[1:]
	print "input artists are", artist_names

depth = 2 #change depth at will

artists_ids = []
for artist in artist_names:
	artists_id = fetchArtistId(artist)
	artists_ids.append(artists_id)

edgeList_list = []
for i in range(len(artists_ids)):
	artist_id = artists_ids[i]
	edge_list = getEdgeList(artist_id,depth)
	edgeList_list.append(edge_list)

concat_Edgelists = edgeList_list[0]
#concat_Edgelists.columns = ['artist', 'related_artist']
for i in range(len(edgeList_list)):
	put_together = combineEdgeLists(concat_Edgelists, edgeList_list[i])
	concat_Edgelists = put_together

g = pandasToNetworkX(concat_Edgelists)

random_artists = []
for i in range(30):
	random_artist = randomCentralNode(g)
	random_artists.append(random_artist)

artist_names = []
album_list = []
for artist_id in random_artists:
	artist = fetchArtistInfo(artist_id)
	artist_name = artist['name']
	artist_names.append(artist_name)
	album_id_list = fetchAlbumIds(artist_id)
	random_album = (random.choice(album_id_list))
	random_album_info = fetchAlbumInfo(random_album) 
	random_album_name = random_album_info['name']
	tupl = (random_album_name, random_album)
	album_list.append(tupl)

random_track_list = []
for album in album_list:
	get_album_tracks_url = 'https://api.spotify.com/v1/albums/' + album[1] + '/tracks'
	req = requests.get(get_album_tracks_url)
	if req.ok == False: 
		print "Error in get_album_tracks_url Request"
	req.json()
	myjson = req.json()
	get_items = myjson.get('items')
	track_list = []
	for i in range(len(get_items)):
		get_track_name = get_items[i]['name']
		track_list.append(get_track_name)
		random_track = (random.choice(track_list))
	random_track_list.append(random_track)
#print random_track_list
#print len(artist_names), len(album_list), len(random_track_list)

f = open('playlist.csv', 'w', encoding='utf-8')
f.write(u'ARTIST_NAME,ALBUM_NAME,TRACK_NAME\n')
for i in range(len(random_track_list)):
	Artist_Name = artist_names[i]
	Album_Name = album_list[i][0]
	Track_Name = random_track_list[i]
	s = '"'+Artist_Name+'"'+','+'"'+Album_Name+'"'+','+'"'+Track_Name+'"'+'\n'
	f.write(s) 
f.close()