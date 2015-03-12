from flask import Flask, render_template, request, redirect, url_for
import pymysql
import unicodecsv
#import sys
import networkx as nx
import pandas as pd
import random
#from io import open
from artistNetworks import getEdgeList
from analyzeNetworks import randomCentralNode, combineEdgeLists, pandasToNetworkX
from fetchArtist import *
from fetchAlbums import * 

dbname="playlists"
host="localhost"
user="root"
passwd=""
db=pymysql.connect(db=dbname, host=host, user=user, passwd=passwd, charset='utf8')

app = Flask(__name__)


@app.route('/')
def make_index_resp():
    # this function just renders templates/index.html when
    # someone goes to http://127.0.0.1:5000/
    return(render_template('index.html'))


@app.route('/playlists/')
def make_playlists_resp():
    return render_template('playlists.html',playlists=playlists)


@app.route('/playlist/<playlistId>')
def make_playlist_resp(playlistId):
    return render_template('playlist.html',songs=songs)


@app.route('/addPlaylist/',methods=['GET','POST'])
def add_playlist():
    if request.method == 'GET':
        # This code executes when someone visits the page.
        return(render_template('addPlaylist.html'))
    elif request.method == 'POST':
        # this code executes when someone fills out the form
        artistName = request.form['artistName']
        # YOUR CODE HERE
        return(redirect("/playlists/"))



def createNewPlaylist(singer_name):

    cur = db.cursor()
    make_table_playlists = '''CREATE TABLE IF NOT EXISTS playlists (id INTEGER PRIMARY KEY AUTO_INCREMENT, rootArtist VARCHAR(128));'''
    make_table_songs = '''CREATE TABLE IF NOT EXISTS songs (playlistId INTEGER, songOrder INTEGER, artistName VARCHAR(128), albumName VARCHAR(256), trackName VARCHAR(256));'''
    cur.execute(make_table_playlists)
    cur.execute(make_table_songs)

    depth = 2
    artists_id = fetchArtistId(ArtistName)
    edge_list = getEdgeList(artists_id,depth)
    g = pandasToNetworkX(edge_list)
    random_artists = []
    
    limit = 30
    while limit > 0:
        random_artist = randomCentralNode(g)
        album_id_list = fetchAlbumIds(random_artist)
        if album_id_list == []:
            pass
        else:
            random_artists.append(random_artist)
            limit = limit -1

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

    artist_name_in = """INSERT INTO playlists (rootArtist) VALUES ('%s')""" % (ArtistName)
    #playlistId = cur.lastrowid
    cur.execute(artist_name_in)
    com_play = """SELECT MAX(id) FROM playlists;"""
    cur.execute(com_play)
    playlistId = cur.fetchall()
    playlistId = playlistId[0][0]
    for i in range(len(random_track_list)):
        songOrder = i+1
        Artist_Name = '"' + artist_names[i] + '"'
        Artist_Name.replace('\'', "")
        Album_Name = '"' + album_list[i][0] + '"'
        Album_Name.replace('\'', "")
        Track_Name = '"' + random_track_list[i] + '"'
        Track_Name.replace('\'', "")
        sql = """INSERT INTO songs (playlistId, songOrder, artistName, albumName, trackName) VALUES (%s, %s, %s, %s, %s)""" % (playlistId, songOrder, Artist_Name, Album_Name, Track_Name)
        cur.execute(sql)
        db.commit()
        
    cur.close()









if __name__ == '__main__':
    app.debug=True
    app.run()