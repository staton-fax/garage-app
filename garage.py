from flask import Flask, render_template
import json
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='./garage-ui/build/static', template_folder='./garage-ui/build')


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/', defalts={'path': ''})
@app.route('<path:path>')
def catch_all(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))