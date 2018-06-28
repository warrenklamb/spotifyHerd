import csv
import spotify

search_minimum = 10000

def removeDuplicates(list):
    return_list = []

    for id in list:
        if id in return_list: continue
        return_list.append(id)
    return(return_list)

def searchRelatedArtists(artist_search, query):
    related_artists = spotify.getRelatedArtists(artist_search)

    for i, artist in enumerate(related_artists['artists']):
        if len(query)<search_minimum:
            query.append(artist['id'])
        else:
            break

def searchArtistInfo(artist_id):
    search_artist = spotify.getArtist(artist_id)
    artist = {'name': search_artist['name'], 'id': search_artist['id'], 'followers': search_artist['followers']['total'], 'popularity': search_artist['popularity']}

    return(artist)

text_file = open("artists.txt", "r")
artists_query = text_file.read().split('\n')

write_file = csv.writer(open("results.csv", "w"))

while len(artists_query)<search_minimum:
    for id in artists_query:
        searchRelatedArtists(id, artists_query)
        id_search_list = removeDuplicates(artists_query)
        artists_query = id_search_list

search_result_list = []

for id in id_search_list:
    search_result_list.append(searchArtistInfo(id))

for row in search_result_list:
    write_file.writerow([{'name': row['name'], 'id': row['id'], 'followers': row['followers'], 'popularity': row['popularity']}])