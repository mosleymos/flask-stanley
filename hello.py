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

#-------------------------------------------------------------------------------
port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
	#app.run()
