from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, flash, redirect, request, abort, jsonify, send_file, Response
import  numpy as np
import secrets
import os
import string
import time
import io
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from Decentralised_App import app, db
from models import Field


def create_figure():
	field = Field.query.filter_by(number=1).first()
	fig = Figure()
	axis = fig.add_subplot(1, 1, 1)
	xs = [x for x in range(len(field.datapoints))]
	ys = field.datapoints
	axis.plot(xs, ys)
	return fig

@app.route("/", methods=["GET", "POST"])
def home():
	fig = create_figure()
	output = io.BytesIO()
	FigureCanvas(fig).print_png(output)
	return Response(output.getvalue(), mimetype='image/png')

@app.route("/register/<int:FieldID>", methods=['GET', 'POST'])
def register(FieldID):
	field = FieldID
	datapoints = []
	timestamps = []
	entry = Field(number=field, datapoints=datapoints, timestamps=timestamps)
	db.session.add(entry)
	db.session.commit()
	return {"Status" : f"Successfully created {field} channel"}

@app.route("/addPoint/<int:FieldID>/<float:data>", methods=["GET", "POST"])
def addPoint(FieldID, data):
	field = Field.query.filter_by(number=FieldID).first()
	stored = list(field.datapoints)
	stored.append(data)
	field.datapoints = list(stored)
	t = time.localtime()
	current_time = time.strftime("%H:%M:%S", t)
	stored = list(field.timestamps)
	stored.append(current_time)
	field.timestamps = list(stored)
	db.session.commit()


	return {"Status" : f"Successfully entered {data} in field={FieldID}"}

