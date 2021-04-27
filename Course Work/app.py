import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:////Users/yazhinigopal/Desktop/DAV Bootcamp/9 SQLite & Flask/surfs_up/Course Work/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

app = Flask(__name__)
@app.route('/')
def welcome():
    return(
    '''
    <h1>Welcome to the Climate Analysis API!</h1>
    <h3>Available Routes:</h3>
    <i>/api/v1.0/precipitation<br>
    /api/v1.0/stations<br>
    /api/v1.0/tobs<br>
    /api/v1.0/temp/start/end</i>
    ''')

@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()
    session.close()
    precip = {date:prcp for date,prcp in precipitation}
    return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session\
    .query(Measurement.tobs)\
    .filter(Measurement.station == 'USC00519281')\
    .filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start,end):
    sel =[func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)]
    results = session\
    .query(*sel)\
    .filter(Measurement.date >= start)\
    .filter(Measurement.date <= end)\
    .all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

if __name__ == "__main__":
    app.run(debug=True)