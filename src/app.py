from flask import Flask
from flask import render_template
from flask import send_file
from flask import send_from_directory
from flask import request

import json
import glob
from os.path import basename

app = Flask(__name__)

@app.route('/designs')
def designs():
    return render_template('designs.html',
            designs=[basename(x) for x in glob.glob('options/*')])

@app.route('/designs/static/<file>')
def static_file(file):
    return send_from_directory('static', file)

@app.route('/designs/options/<file>')
def options_file(file):
    return send_from_directory('options', file)

@app.route('/designs/vote/<design>')
def designs_vote(design):
    with open('votes.json', 'r') as fp:
        votes = json.load(fp)

    ip = request.headers.get('X-Real-IP', '0.0.0.0')

    votes[ip] = design

    with open('votes.json', 'w+') as fp:
        json.dump(votes, fp)

    print(votes)
    return json.dumps({ ip: design})

# for development purposes only... in production, stylesheet will be served by nginx
@app.route('/styles.css')
def styles():
    return send_file('styles.css')

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
