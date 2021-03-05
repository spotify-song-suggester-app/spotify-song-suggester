'''SQLAlchemy Database for Spotify song suggestor'''

from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy()


# Table using SQLAlchemy syntax 
class Songs(DB.Model):
    '''Spotify Song DB'''
    id = DB.Column(DB.String, primary_key=True)
    acousticness = DB.Column(DB.Float, nullable=False)
    artists = DB.Column(DB.String, nullable=False)
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
    speechiness = DB.Column(DB.Float, nullable=False)
    tempo = DB.Column(DB.Float, nullable=False)
    valence = DB.Column(DB.Float, nullable=False)
    year = DB.Column(DB.Integer, nullable=False)

    def __repr__(self):
        return f'<Song: {self.name}>'
