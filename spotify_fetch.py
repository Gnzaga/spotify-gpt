import requests
import credentials


#generates access token for spotify api using client id and client secret
def get_access_token(client_id, client_secret):
    url = 'https://accounts.spotify.com/api/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'grant_type': 'client_credentials'}
    response = requests.post(url, headers=headers, data=payload, auth=(client_id, client_secret))
    access_token = response.json().get('access_token')
    return access_token

#returns access token for spotify api
def get_my_access_token():
    return get_access_token(credentials.spotify_client_id, credentials.spotify_client_secret)


