from Decentralised_App import db
from sqlalchemy_utils import ScalarListType
import sqlalchemy_utils

class Field(db.Model):
	__tablename__ = 'user'
	number = db.Column(db.Integer, primary_key=True)
	datapoints = db.Column(ScalarListType(float))
	timestamps = db.Column(ScalarListType(str))


	def __repr__(self):
		return f"Field = {self.datapoints}"