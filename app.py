from flask import Flask, url_for, jsonify, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# Can it solve it within it's own memory?
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory'
# Database
db = SQLAlchemy(app)
# Schema Variable
ma = Marshmallow(app)

class Message(db.Model):
    conversation_id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer)
    # character limit is 500 
    sender_name = db.Column(db.String(500), default='Guest')
    content = db.Column(db.String(500), nullable=False)
    time_sent = db.Column(db.String)

class MessageSchema(ma.Schema):
    class Meta:
        fields = ('conversation_id', 'sender_id', 'sender_name', 'content', 'time_sent')

my_message_schema = MessageSchema(many=True)

# Make table here
@app.route('/')
def create_database():
    db.create_all()
    return 'New Table Has Been Made'

@app.route('/messages')
def get_messages():
    # get messages from table
    message_entries = Message.query.all()
    result = my_message_schema.dump(message_entries)
    # return final product in json format
    return jsonify(result)

if __name__ == "__main__":
    # db.create_all()
    app.run()