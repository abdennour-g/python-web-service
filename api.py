import flask
from flask import request, jsonify,Flask
from flask_cors import CORS, cross_origin
from dao import *
from beans import *

app = flask.Flask(__name__)
cors = CORS(app, resources={r'/*': {'origins': '*'}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['DEBUG'] = True
bdd=dao()
data=bdd.affJson()

@app.route('/', methods=['GET','POST'])
@cross_origin()
def home():
    #if request.method == 'GET':
    #    return jsonify(data)
    if request.method == 'POST':
        print('response from python flask')
        newpers=person( request.form.get('cin'),
            request.form.get('nom'),
            request.form.get('prenom'),
            request.form.get('tel'),
            request.form.get('email'),
            )
        bdd.insertPers(newpers)   
        print(newpers)
    response = flask.jsonify(bdd.affJson())
    #response.headers.add('Access-Control-Allow-Origin', '*')
    return response
app.run()