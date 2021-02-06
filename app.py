from flask import Flask,render_template
from main import top_song
import os

app=Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello_world():
    
    song= top_song()
    return render_template(
        "index.html",
        my_song_name=song['song_name'],
        my_song_artist=song['song_artist'],
        my_preview_url=song['preview_url'],
        )

app.run(
    host=os.getenv('IP',"0,0,0,0"),
    port=int(os.getenv("PORT",8080)),
    debug=True
    )