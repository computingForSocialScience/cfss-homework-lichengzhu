import requests
import pandas as pd
import numpy as np

def getRelatedArtists(artistID):
	url_base = 'https://api.spotify.com/v1/artists/'
	artist_ID = str(artistID)
	end_url = '/related-artists'
	url = url_base + artist_ID + end_url
	req = requests.get(url)
	if req.ok == False:
		print 'Error'
	req_json = req.json()
	get_artists = req_json.get('artists')
	related_artist_list = []
	for i in range(len(get_artists)):
		get_line = get_artists[i]
		get_id = get_line['id']
		related_artist_list.append(get_id)
	return related_artist_list

def getDepthEdges(artistID, depth):

	n = 0
	master_list = []
	while n < depth:
		
		# counting control
		if n == depth: break
		
		# first level:
		if master_list == []:
			level_one_related_list = getRelatedArtists(artistID)
			for level_one_i in level_one_related_list:
				master_list.append((artistID, level_one_i))
		
		# second level and beyond
		else:
			new_list = []
			for item in master_list:
				artistID = item[1]
				item_level_list = getRelatedArtists(artistID)
				for i in item_level_list:
					if (artistID, i) in master_list:
						pass
					else:
						new_list.append((artistID, i))
			master_list.extend(new_list)

		n += 1

	#print(len(master_list))
	#print(master_list)
	return(master_list)

# getDepthEdges('2mAFHYBasVVtMekMUkRO9g', 2)
# (id = '2mAFHYBasVVtMekMUkRO9g', depth = 1) gives me a list with 20 tuples
# (id = '2mAFHYBasVVtMekMUkRO9g', depth = 2) gives me a list with 420 tuples
# (id = '2mAFHYBasVVtMekMUkRO9g', depth = 3) gives me a list of 2800 tuples)



def getEdgeList(artistID, depth):
	data = getDepthEdges(artistID, depth)
	#print(data)
	data = np.array(data)
	converted_data = pd.DataFrame(data)
	#print(converted_data)
	return(converted_data)

def writeEdgeList(artistID, depth, filename):
	data = getEdgeList(artistID, depth)
	data.to_csv(filename, index = False, header = ['artist', 'related_artist'])

#writeEdgeList('2mAFHYBasVVtMekMUkRO9g', 2, 'out.csv')