import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='b0ef72abfbc044e581d0e31d1144d39f', client_secret='89aae697ec7142eeaeace0d643f8bcbb')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

country = 'US'
search_limit = 20

def getArtist(artist_id):
    return_artist = sp.artist(artist_id)
    return(return_artist)

def getRelatedArtists(artist_id):
    return_artists = sp.artist_related_artists(artist_id)
    return(return_artists)

def getArtistTopTracks(artist_id):
    return_top_tracks = sp.artist_top_tracks(artist_id, country)
    return(return_top_tracks)

def getArtistAlbums(artist_id):
    return_albums = sp.artist_albums(artist_id, None, country, search_limit, 0)
    return(return_albums)

def getAlmbum(album_id):
    return_album = sp.album(album_id)
    return(return_album)

def getAlbumTracks(album_id):
    return_album_tracks = sp.album_tracks(album_id, 50, 0)
    return(return_album_tracks)
