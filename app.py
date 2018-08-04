import os

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from textblob import TextBlob
import sys
import os
import urllib




from flask import Flask
from flask import render_template

app = Flask(__name__)

#-------------------------------------------------------------------------------
#@app.route('/')
#def hello():
#	return "Hello World"


API_KEY = "AIzaSyBdDDnfLMXZ_z43CYWiDpuDteqOiNiHNa8"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
QUERY_TERM = "young princess"     ### Search youtube for these ..... and create a playlist
videos_links = []



@app.route('/')
@app.route('/index')
def index():

    return render_template('pages/index.html')


@app.route('/tell_me_about_your_movie')
def tell_me_about_your_movie():
    return render_template('pages/tell_me_about_your_movie.html')

@app.route('/stanley_is_working')
def stanley_is_working():
    return render_template('pages/stanley_is_working.html')


@app.route('/your_trailer')
def your_trailer():
    return render_template('pages/your_trailer.html')



###################### ----------------------------------------------########################


def search_by_keyword( input_text):

    input_blob = TextBlob (input_text)
    search_terms = input_blob.noun_phrases

    youtube = build( YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

    videos = []
    for line in search_terms:
        print line
        search_response = youtube.search().list(
          q=line,
          part="id,snippet",
          maxResults=10
        ).execute()

        link= "https://www.youtube.com/watch?v="

        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                full_link = link+search_result["id"]["videoId"]
                videos.append(full_link)

    return videos


def download_videos(videos):
	#videos = search_by_keyword()
	cmd = """ youtube-dl  --get-filename -o "%(title)s.%(ext)s" """

	for v in videos:
		cmd = cmd + v
		print cmd
		os.system(cmd)




#-------------------------------------------------------------------------------
port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))



