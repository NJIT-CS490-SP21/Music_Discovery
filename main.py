import requests
import os
from dotenv import load_dotenv,find_dotenv
import spotify
import random


def top_song():
    load_dotenv(find_dotenv())
    AUTH_URL = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('ID'),
        'client_secret': os.getenv('SECRET'),
    })
    
    auth_response_data = auth_response.json()
    
    # save the access token
    access_token = auth_response_data['access_token']
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    
    #print(access_token)
    
    #1#URL-future = "1RyvyyTE3xzB2ZywiAwp0i?si=MOw3M23qRDWDhR0XmrK__g"
    #2#URL-offset= "4DdkRBBYG6Yk9Ka8tdJ9BW?si=C2j2gxKlT0OI_zXnGOTKPg"
    #3#URL-travisScott="0Y5tJX1MQlPlqiwlOH1tJY?si=wyJ6pFB_SF6zQHDklMxewQ"
    #id="246dkjvS1zLTtiykXe5h60"
    
    URL1 = "https://api.spotify.com/v1/artists/1RyvyyTE3xzB2ZywiAwp0i/top-tracks"
    URL2 = "https://api.spotify.com/v1/artists/4DdkRBBYG6Yk9Ka8tdJ9BW/top-tracks"
    URL3= "https://api.spotify.com/v1/artists/0Y5tJX1MQlPlqiwlOH1tJY/top-tracks"
    URL = [URL1,URL2,URL3]
    params ={
        'market': 'US',
    }
    
    
    response = requests.get(random.choice(URL) , headers=headers,params=params) 
    data = response.json()
    
    #Song name
    song_name=data['tracks'][0]['name']
    #return(song_name)
    
    #song artists
    song_artist=data['tracks'][0]['artists'][0]['name']
    #return(song_artist)
    
    #print(data['tracks'][0]['images'][0]['height'])
    
    #preview URL
    preview_url=data['tracks'][0]['preview_url']
    #return(preview_url)
    return{
        'song_name':song_name,
        'song_artist':song_artist,
        'preview_url':preview_url,
    }

