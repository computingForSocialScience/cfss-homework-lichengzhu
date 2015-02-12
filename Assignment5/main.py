import sys
from fetchArtist import fetchArtistId, fetchArtistInfo
from fetchAlbums import fetchAlbumIds, fetchAlbumInfo
from csvUtils import writeArtistsTable, writeAlbumsTable
from barChart import plotBarChart

if __name__ == '__main__':
    artist_names = sys.argv[1:]
    print "input artists are ", artist_names
    # YOUR CODE HERE
    artist_list = []
    album_list = []
    for hahaha in artist_names:
    	
    	get_artist_id = fetchArtistId(hahaha)
    	get_artist_info = fetchArtistInfo(get_artist_id)
    	
    	artist_list.append(get_artist_info)
    	
    	get_album_ids = fetchAlbumIds(get_artist_id)
    	
    	for album in get_album_ids:
    		get_album_info = fetchAlbumInfo(album)
    		album_list.append(get_album_info)

    writeArtistsTable(artist_list)
    writeAlbumsTable(album_list)
    #getBarChartData()
    plotBarChart()
    

