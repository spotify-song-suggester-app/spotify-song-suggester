'''Main app/routing file for Spotify search app'''

from flask import Flask, render_template, request
from os import getenv
from .models import DB
from .cleandf import *


def create_app():
    '''Create flask app'''
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'spotify_db.sqlite3' 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)
    
    @app.route('/')
    def root():
        '''At end point '/' this is the home screen'''
        create_table()
        return render_template('search.html')
    
    # @app.route('/results')
    # def results():
        # TODO - take user input as string 
        # run prediction on input
        # return top 10 songs suggested

    return app