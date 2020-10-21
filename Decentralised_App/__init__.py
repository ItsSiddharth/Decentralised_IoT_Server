from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///FieldData.db'


from Decentralised_App import routes