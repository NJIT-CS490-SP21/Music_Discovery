from flask import Flask,render_template
from main import top_song
import os

app=Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello_world():
    
    offset_url="https://tse2.mm.bing.net/th?id=OIP.vjqTJToCvwG4H00oH1Z4WgHaHa&pid=Api&P=0&w=300&h=300"
    travis_url="https://tse3.mm.bing.net/th?id=OIP.NWMTwpG460SMaOxLd1SEKwHaEK&pid=Api&P=0&w=368&h=208"
    future_url="https://i.redd.it/non7ml0cjsa41.png"
    song= top_song()
    return render_template(
        "index.html",
        song_name=song['song_name'],
        song_artist=song['song_artist'],
        preview_url=song['preview_url'],
        future=future_url,
        travis=travis_url,
        offset=offset_url,
        )

app.run(
    host=os.getenv('IP',"0,0,0,0"),
    port=int(os.getenv("PORT",8080)),
    debug=True
    )