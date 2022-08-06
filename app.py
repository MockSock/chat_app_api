from dataclasses import fields
import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# Database
db = SQLAlchemy(app)
# Schema Variable
ma = Marshmallow(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'

class Message(db.Model):
    conversation_id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer)
    # character limit is 500 
    sender_name = db.Column(db.String(500))
    content = db.Column(db.String(500))
    time_sent = db.Column(db.String)

class MessageSchema(ma.Schema):
    class Meta:
        fields = ('conversation_id', 'sender_id', 'sender_name', 'content', 'time_sent')

my_message_schema = MessageSchema(many=True)

# Control Method
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/messages')
def getMessages():
    return 'I will be your messages soon'

if __name__ == "__main__":
    db.create_all()
    app.run()