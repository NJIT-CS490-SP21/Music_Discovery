# Project1-Milestone2

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
* npm install -g heroku

## Launch:
In order to run the project1 clearly, you need to create a spotify rest API and create a simple app, export your client-id and client-secret in a .env file,
Export your client id as "ID" in the .env file and export client secret as "SECRET" in .env.You also need to create a Genius API and a create a client app, have your client id and client secret exported in the .env file. You also need
to generate a access token which will be on your dashboard, then export it on the .env file. You need to export each of them as "genius-ID", "genius-Secret" and "genius-Token".
Save all your files.
Now you can run app.py with the command python app.py
After that click on preview and you should be able to see the webpage.

## Acknowledgements:
1.Getting two or more top song from one artist .
2.Improve current project to have a playlist of top songs from the artist that user inputs. I would like to implement a List of Current User's Playlists
or list of Spotify playlists tagged with a particular category.

##  Detailed description:
#### Issue with the Keyerror: access_token
The error I was getting was 'keyerror: access_token'.
To fix this issue I thought I cannot connect to the Spotify API so I hardcode my client-id and client-secret into my app which is not recommended.
Also I didnt have load_dotenv(find_dotenv()) line of code so my os.getenv() can find the id and secret in the hidden .env file,
this sound very simple bug but it took me hours to fidn the issue.
The resource that help me out is: 
https://www.youtube.com/watch?v=6hFuJwNt0UA&feature=youtu.be

#### Issue with getting the desired information.
This issue requires understanding of what I needed for this project. My problem was doing everything at the same time.
But I tried to put it in pieces, first I find the spotofy id of my favourite artist, then I put them in a list so I can randomly
choose my favourite artist. Then I utilize the access token to send a GET request to find my artists to songs.
The resources that help me out are:
https://developer.spotify.com/documentation/web-api/reference/#category-artists
https://dev.to/arvindmehairjan/how-to-play-spotify-songs-and-show-the-album-art-using-spotipy-library-and-python-5eki

#### Issue on passing info from the main to the app and eventually showing them on the webpage
Once I finished main.py I had everuthing I needed but I didnt know how to utilize those output in order to run flask and 
connect to the html to show my output on the webpage. For this one I tried to understand the example from our class, where 
we trying to find the specific article in the New york times api. This example helped me to how to return my variable from 
main so I can use them in the app and then assign them in html.
The resource that help me out is:
https://github.com/NJIT-CS490-SP21/lect5-demo-nyt



