"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, Queue
from twilio import twiml
from twilio.rest import Client
from twilio.twiml.messaging_response import Message, MessagingResponse

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

queue = Queue(mode="FIFO")

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/new', methods=['POST'])
def addQueue():
    user = request.get_json()

    queue.enqueue(user)

    body = request.get_json()

    if body is None:
        raise APIException("Its empty", status_code=400)
    if 'name' not in body:
        raise APIException('You need to add name', status_code=400)
    if 'phone' not in body:
        raise APIException('you need to specify the phone', status_code=400)
    queue.enqueue(body)
    return "ok", 200


    return jsonify(user)

@app.route('/next', methods=['GET'])
def deleteQueue():
    queue.dequeue()
    return jsonify(queue.get_queue())

@app.route('/all', methods=['GET'])
def getAllFromList():
    return jsonify(queue.get_queue())
    #aux = queue.get_queue()
    #return jsonify(aux)

# Download the helper library from https://www.twilio.com/docs/python/install



# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACf21deb2904b14ad2094c6e6ed2620d76'
auth_token = 'f16a6a1ab906dd3df0f8070308d3a701'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+17544659541',
                     to='+17862021287'
                 )

print(message.sid)


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT)
