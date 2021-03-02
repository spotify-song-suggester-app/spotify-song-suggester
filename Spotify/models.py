'''SQLAlchemy Database for Spotify song suggestor'''

from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import re
import numpy as np
import sqlite3

DB = SQLAlchemy()

# Wrangle function from Austin to clean Spotify Song data
def wrangle(filename='data.csv'):
    # read csv
    df = pd.read_csv(filename, parse_dates=['release_date'], index_col='id')

    # pull artist names out of list
    df['artists'] = [re.sub('^\[\'|\["', '', i) for i in df['artists']]
    df['artists'] = [re.sub('\'\]|"\]$', '', i) for i in df['artists']]

    # convert duration from ms to min
    df['duration_min'] = df['duration_ms'] / 60000
    df['duration_min'] = df['duration_min'].round(2)

    # drop duplicate values
    df.drop_duplicates(inplace=True)

    # drop duration_ms and release_date
    df.drop('duration_ms', axis=1, inplace=True)
    df.drop('release_date', axis=1, inplace=True)

    return df

df = wrangle()
conn = sqlite3.connect('spotify_db.sqlite3')
curs = conn.cursor()
df.to_sql('Songs', conn, if_exists='replace', index=False)


# Table using SQLAlchemy syntax 
class Song(DB.Model):
    '''Spotify Song DB'''
    id = DB.Column(DB.String, primary_key=True)
    acousticness = DB.Column(DB.Float, nullable=False)
    artist = DB.Column(DB.String, nullable=False)
    danceability = DB.Column(DB.Float, nullable=False)
    duration_min = DB.Column(DB.Float, nullable=False)
    energy = DB.Column(DB.Float, nullable=False)
    explicit = DB.Column(DB.Integer, nullable=False)
    instrumentalness = DB.Column(DB.Float, nullable=False)
    key = DB.Column(DB.Integer, nullable=False)
    liveness = DB.Column(DB.Float, nullable=False)
    loudness = DB.Column(DB.Float, nullable=False)
    mode = DB.Column(DB.Integer, nullable=False)
    name = DB.Column(DB.String, nullable=False)
    popularity = DB.Column(DB.Integer, nullable=False)
    release_date = DB.Column(DB.DateTime, nullable=False)
    speechiness = DB.Column(DB.Float, nullable=False)
    tempo = DB.Column(DB.Float, nullable=False)
    valence = DB.Column(DB.Float, nullable=False)
    year = DB.Column(DB.Integer, nullable=False)
