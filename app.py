from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# Database
db = SQLAlchemy(app)
# Schema Variable
ma = Marshmallow(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 

class Messages(db.Model):
    

if __name__ == "__main__":
    db.create_all()
    app.run()