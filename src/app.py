from flask import Flask
from flask import render_template
from flask import send_file
from flask import send_from_directory
from flask import request

import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/designs')
def designs():
    return render_template('designs.html')

@app.route('/styles.css')
def styles():
    return send_file('./styles.css')

@app.route('/static/<file>')
def static_file(file):
    return send_from_directory('static', file)

@app.route('/designs/vote/<design>')
def designs_vote(design):
    with open('votes.json', 'r') as fp:
        votes = json.load(fp)

    votes[request.environ.get('HTTP_X_REAL_IP', request.remote_addr)] = design

    with open('votes.json', 'w+') as fp:
        json.dump(votes, fp)

    print(votes)
    return json.dumps(votes)

@app.route('/designs/votes')
def designs_votes():
    with open('votes.json', 'r') as fp:
        votes = json.load(fp)

    r = {}

    for ip in votes.keys():
        if votes[ip] in r.keys():
            r[votes[ip]] += 1
        else:
            r[votes[ip]] = 1

    if request.args.get('json') is not None:
        return json.dumps(r)

    return render_template('designs_votes.html', votes=r)
