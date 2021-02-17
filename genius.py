import requests
import os
from dotenv import load_dotenv,find_dotenv
import random

load_dotenv(find_dotenv())

def top_song_lyrics(song_artist,song_name):
    token=os.getenv("genius-Token")
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + str(token)}
    search_url = base_url + '/search'
    data = {'q': song_artist + ' ' + song_name}
    response = requests.get(search_url, data=data, headers=headers)
    data = response.json()
    song_lyrics_link=data['response']['hits'][0]['result']['url']
    return {
        'song_lyrics_link': song_lyrics_link,
    }
    
def top_song():
    AUTH_URL = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('ID'),
        'client_secret': os.getenv('SECRET'),
    })
    
    auth_response_data = auth_response.json()
    
    access_token = auth_response_data['access_token']
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
 
    URL1= "https://api.spotify.com/v1/artists/0VRj0yCOv2FXJNP47XQnx5/top-tracks"
    URL2 = "https://api.spotify.com/v1/artists/4DdkRBBYG6Yk9Ka8tdJ9BW/top-tracks"
    URL3= "https://api.spotify.com/v1/artists/0Y5tJX1MQlPlqiwlOH1tJY/top-tracks"
    URL = [URL1,URL2,URL3]
    params ={
        'market': 'US',
    }
    
    response = requests.get(random.choice(URL) , headers=headers,params=params) 
    data = response.json()
  

    song_name=data['tracks'][0]['name']
    song_artist=data['tracks'][0]['artists'][0]['name']
  
    song_img=data['tracks'][0]['album']['images'][0]['url']
    
    preview_url=data['tracks'][0]['preview_url']
 
    return{
        'song_name':song_name,
        'song_artist':song_artist,
        'song_img':song_img,
        'preview_url':preview_url,
    }

