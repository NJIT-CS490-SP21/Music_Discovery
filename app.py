from flask import Flask,render_template
from main import top_song,top_song_lyrics
import os

app=Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello_world():
    song= top_song()
    song_artist=song['song_artist']
    song_name=song['song_name']
    lyrics=top_song_lyrics(song_artist,song_name)
    return render_template(
        "index.html",
        song_name=song['song_name'],
        song_artist=song['song_artist'],
        preview_url=song['preview_url'],
        song_img=song['song_img'],
        song_lyrics_link=lyrics['song_lyrics_link']
        )

app.run(
    host=os.getenv('IP',"0,0,0,0"),
    port=int(os.getenv("PORT",8080)),
    debug=True
    )