from flask import Flask, url_for, jsonify, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import cross_origin, CORS

from random_number import createRandomNumber

import os

app = Flask(__name__)
CORS(app)

# The path has to be coded into a variable according to this:
# https://stackoverflow.com/questions/18208492/sqlalchemy-exc-operationalerror-operationalerror-unable-to-open-database-file
file_path = os.path.abspath(os.getcwd())+'\messages.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path

# Database
db = SQLAlchemy(app)
# Schema Variable
ma = Marshmallow(app)

class Message(db.Model):
    # need something to differentiate different messages
    message_id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer)
    # character limit is 500 
    sender_name = db.Column(db.String(500), default='Guest')
    content = db.Column(db.String(500), nullable=False)
    time_sent = db.Column(db.String)

# Some stuff says to call this right after making the database?
db.create_all()

class MessageSchema(ma.Schema):
    class Meta:
        fields = ('message_id','sender_id', 'sender_name', 'content', 'time_sent')

my_message_schema = MessageSchema(many=True)


# need a / one 
@app.route('/')
def hello_world():
    return "Hello World"
    
# Get Messages
@cross_origin()
@app.route('/messages')
def get_messages():
    # get messages from table
    message_entries = Message.query.all()
    result = my_message_schema.dump(message_entries)
    # return final product in json format
    return jsonify(result)

# Post a new message to db
@cross_origin()
@app.route('/new_message', methods=['POST'])
def post_message():
    req = request.get_json()
    message_id = createRandomNumber()
    sender_id = req['sender_id']
    sender_name = req['sender_name']
    time_sent = req['time_sent']
    content = req['content']
    new_entry = Message(message_id= message_id,sender_id=sender_id, sender_name=sender_name, time_sent=time_sent, content=content)

    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for('get_messages'))

if __name__ == "__main__":
    app.run()