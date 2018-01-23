from flask import Flask
app = Flask(__name__)

import json
import random

@app.route('/')
def hello_world():
 return 'Hello World!'

@app.route('/dice/')
def roll_dice():
	return json.dumps({'dice 1': random.randint(1,6),  'dice 2': random.randint(1,6)})

if __name__ == '__main__':
 app.debug = True
 app.run()
