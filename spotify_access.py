import requests
from collections import Counter
import spotify_fetch

#midsummer refresh
#playlist_example = 'https://open.spotify.com/playlist/3iN5bQqXjh7OVzmOFVfKOn?si=3135f7c2e53241c6'

#moving
#playlist_example = 'https://open.spotify.com/playlist/1lLqCXNPoAM0NKnGjWAG71?si=144b4bf1f426447f'

#RU n B
playlist_example = 'https://open.spotify.com/playlist/1YbYHB590UlACSY5WcALxI?si=043340c2aa1944ff'

#Dead end
#playlist_example = 'https://open.spotify.com/playlist/6a7i0rbYPnt8lj7SSzJiO5?si=46ef16f2916c4d5f'

#hunnies & high rises
#playlist_example = 'https://open.spotify.com/playlist/6eXgiTmlhzJC96mYhyy5xH?

#i'm tired
#playlist_example ='https://open.spotify.com/playlist/0Z0IO8nny2x0TuQQwT9ODA?si=96e3b5f019054189'

access_token = spotify_fetch.get_my_access_token()  # This is the access token you'll use to make requests to the Spotify API


#https://open.spotify.com/playlist/playlist_id
def extract_playlist_id(playlist_url):
    return playlist_url.split("playlist/")[1].split("?")[0]  # Adjust based on actual URL format

def get_playlist_json(playlist_id, access_token):
    url = f'https://api.spotify.com/v1/playlists/{playlist_id}'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    return response.json()  # This contains detailed info about the playlist

def extract_track_names(playlist_json):
    track_names = [item['track']['name'] for item in playlist_json['tracks']['items']]
    return track_names

def extract_track_href(playlist_json):
    track_href = [item['track']['href'] for item in playlist_json['tracks']['items']]
    return track_href

def extract_track_ids(playlist_json):
    track_ids = [item['track']['id'] for item in playlist_json['tracks']['items']]
    return track_ids

def extract_album_names(playlist_json):
    album_names = [item['track']['album']['name'] for item in playlist_json['tracks']['items']]
    return album_names

def extract_track_durations(playlist_json):
    track_durations_ms = [item['track']['duration_ms'] for item in playlist_json['tracks']['items']]
    return track_durations_ms


#https://api.spotify.com/v1/audio-features/{id}
def get_audio_feature(track_id, access_token):
    url = f'https://api.spotify.com/v1/audio-features/{track_id}'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    return response.json()  # This contains detailed info about the track's audio features

#can use comma separated list of id's to get multiple tracks audio features
def get_multiple_tracks_audio_features(track_ids, access_token):
    url = f'https://api.spotify.com/v1/audio-features?ids={",".join(track_ids)}'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    return response.json()  # This contains detailed info about the tracks' audio features

def extract_artist_ids(playlist_json):
    artist_ids = [item['track']['artists'][0]['id'] for item in playlist_json['tracks']['items']]
    return artist_ids


def get_artist_details(artist_id, access_token):
    url = f'https://api.spotify.com/v1/artists/{artist_id}'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    return response.json()  # This contains detailed info about the artist, including genres

def get_multiple_artists_details(artist_ids, access_token):
    # Spotify's limit for fetching multiple artists in one request
    SPOTIFY_ARTIST_FETCH_LIMIT = 50
    artist_details_list = []

    # Splitting the artist_ids into chunks of 50
    for i in range(0, len(artist_ids), SPOTIFY_ARTIST_FETCH_LIMIT):
        batch = artist_ids[i:i + SPOTIFY_ARTIST_FETCH_LIMIT]
        url = f'https://api.spotify.com/v1/artists?ids={",".join(batch)}'
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            artist_details_list.extend(response.json()['artists'])
        else:
            print(f"Error fetching artists: {response.status_code}")
            # Handle error appropriately

    return {'artists': artist_details_list}


def extract_all_artist_ids(playlist_json):
    all_artist_ids = []
    for item in playlist_json['tracks']['items']:
        artist_ids = [artist['id'] for artist in item['track']['artists']]
        all_artist_ids.extend(artist_ids)
    return all_artist_ids



def get_audio_features_json(playlist_json, access_token):
    track_href = extract_track_href(playlist_json)
    audio_features = [get_audio_features(href, access_token) for href in track_href]
    return audio_features

def display_audio_features(audio_features):
    for feature in audio_features:
        print(feature)

#matches audio features to their track, but also adds the artist's genres found in the track object
def match_audio_features_to_tracks_and_artist(playlist_json, audio_features):
    track_names = extract_track_names(playlist_json)
    artist_ids = extract_all_artist_ids(playlist_json)
    artist_details = get_multiple_artists_details(artist_ids, access_token)
    matched_audio_features = {}
    for i in range(len(track_names)):
        track_name = track_names[i]
        features = audio_features['audio_features'][i]
        artist_id = artist_ids[i]
        artist = [artist['genres'] for artist in artist_details['artists'] if artist['id'] == artist_id]
        matched_audio_features[track_name] = [features, artist, artist_details['artists'][i]['name']]
    return matched_audio_features


def display_audio_features_and_genre_details(matched_audio_features):
    for track, features in matched_audio_features.items():
        print(f'Track: {track}')
        print(f'Audio Features: {features[0]}')
        print(f'Artist: {features[2]}')
        print(f'Genres: {features[1]}')
        print('-----------------------------------------')



def aggregate_genres(artists_genres):
    all_genres = []
    for genres in artists_genres.values():
        all_genres.extend(genres)
    return all_genres


def count_genre_occurrences(all_genres):
    genre_counts = Counter(all_genres)
    return genre_counts

def get_top_genres(genre_counts, n=5):
    return genre_counts.most_common(n)



def find_average_top_n_genres(artists_genres, n):
    all_genres = aggregate_genres(artists_genres)
    genre_counts = count_genre_occurrences(all_genres)
    top_5_genres = get_top_genres(genre_counts, n)
    return top_5_genres

def find_average_top_n_genres_names(artists_genres, n):
    top_n_genres = find_average_top_n_genres(artists_genres, n)
    return [genre[0] for genre in top_n_genres]

def display_top_genres(url):
    playlist_id = extract_playlist_id(url)
    playlist_json = get_playlist_json(playlist_id, access_token)
    artist_ids = extract_all_artist_ids(playlist_json)
    artist_details = get_multiple_artists_details(artist_ids, access_token)
    artists_genres = {artist['name']: artist['genres'] for artist in artist_details['artists']}
    top_genres = find_average_top_5_genres(artists_genres)
    print(top_genres)

def display_top_genres_from_json(playlist_json):
    artist_ids = extract_all_artist_ids(playlist_json)
    artist_details = get_multiple_artists_details(artist_ids, access_token)
    #print(artist_details)
    artists_genres = {artist['name']: artist['genres'] for artist in artist_details['artists']}
    top_genres = find_average_top_5_genres(artists_genres)
    print(top_genres)

def aggregate_audio_features(audio_features):
    # Initialize a dictionary to hold the sum of each feature
    aggregated_features = {
        "acousticness": 0,
        "danceability": 0,
        "energy": 0,
        "instrumentalness": 0,
        "liveness": 0,
        "loudness": 0,
        "speechiness": 0,
        "tempo": 0,
        "valence": 0
    }
    
    track_count = len(audio_features)
    
    for feature in audio_features:
        for key in aggregated_features.keys():
            aggregated_features[key] += feature.get(key, 0)
    
    # Calculate the average of each feature
    averaged_features = {key: value / track_count for key, value in aggregated_features.items()}
    
    return averaged_features

def display_aggregated_audio_features(audio_features):
    aggregated_features = aggregate_audio_features(audio_features)
    for key, value in aggregated_features.items():
        print(f'{key}: {value}')


#returns a json of the aggregated audio features and the top genres of the playlist
def get_playlist_audio_features_and_top_genres(playlist_url):
    
    playlist_id = extract_playlist_id(playlist_url)
    playlist_json = get_playlist_json(playlist_id, access_token)
    track_ids = extract_track_ids(playlist_json)
    audio_features = get_multiple_tracks_audio_features(track_ids, access_token)
    artist_ids = extract_all_artist_ids(playlist_json)
    artist_details = get_multiple_artists_details(artist_ids, access_token)
    artists_genres = {artist['name']: artist['genres'] for artist in artist_details['artists']}
    aggregated_audio_features = aggregate_audio_features(audio_features['audio_features'])
    top_genres = find_average_top_n_genres_names(artists_genres, 2)
    return {'audio_features': aggregated_audio_features, 'top_genres': top_genres}


print(get_playlist_audio_features_and_top_genres(playlist_example))

#set up to run tests
'''
playlist_id = extract_playlist_id(playlist_example)
playlist_json = get_playlist_json(playlist_id, access_token)
track_ids = extract_track_ids(playlist_json)
audio_features = get_multiple_tracks_audio_features(track_ids, access_token)


display_top_genres_from_json(playlist_json)
display_aggregated_audio_features(audio_features['audio_features'])
'''


'''
playlist_id = extract_playlist_id(playlist_example)
playlist_json = get_playlist_json(playlist_id, access_token)
track_ids = extract_track_ids(playlist_json)
audio_features = get_multiple_tracks_audio_features(track_ids, access_token)

matched_audio_features = match_audio_features_to_tracks_and_artist(playlist_json, audio_features)

display_audio_features_and_genre_details(matched_audio_features)

'''