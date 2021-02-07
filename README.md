# Project1-Milestone1

## Introduction
This README file contains the main toolchain for a simple music discovery web app that shows song(s) from your favorite artist(s) and link(s) to the preview.

## Technologies:
Project1 is created with:
* pyhton version: 3.6.12
* Flask version: 1.1.2
* AWS cloud9 environment

## Installation:
* pip install requests
* pip install flask
* pip install -U python-dotenv

## Launch:
In order to run the project1 clearly, you need to create a spotify rest API and create a simple app, export your client-id and client-secret in a .env file,
then run main.py with the command python main.py followed by python app.py.
After that click on preview and you should be able to see the webpage.

## Acknowledgements:
The main issue with the projetc1, at least with me, was getting the access_token.
The second issue was how to get your desired information from Spotify.

##  Detailed description:
#### Issue with the Keyerror: access_token
The error I was getting was 'keyerror: access_token'.
To fix this issue I thought I cannot connect to the Spotify API so I hardcode my client-id and client-secret into my app which is not recommended.
Also I didnt have load_dotenv(find_dotenv()) line of code so my os.getenv() can find the id and secret in the hidden .env file,
this sound very simple bug but it took me hours to fidn the issue.
The resource that help me out is: 
(https://www.youtube.com/watch?v=6hFuJwNt0UA&feature=youtu.be)

####Issue with getting the desired information.
This issue requires understanding of what I needed for this project. My problem was doing everything at the same time.
But I tried to put it in pieces, first I find the spotofy id of my favourite artist, then I put them in a list so I can randomly
choose my favourite artist. Then I utilize the access token to send a GET request to find my artists to songs.

(https://developer.spotify.com/documentation/web-api/reference/#category-artists)
(https://dev.to/arvindmehairjan/how-to-play-spotify-songs-and-show-the-album-art-using-spotipy-library-and-python-5eki)





