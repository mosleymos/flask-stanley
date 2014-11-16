import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

#-------------------------------------------------------------------------------
#@app.route('/')
#def hello():
#	return "Hello World"


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

#-------------------------------------------------------------------------------
port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
