'''Main app/routing file for Spotify search app'''

from flask import Flask, render_template, request
from os import getenv
from .models import DB
from .cleandf import *
from .forms import MyForm


def create_app():
    '''Create flask app'''
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'spotify_db.sqlite3' 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/', methods = ['POST', 'GET'])
    def root():
        '''At end point '/' this is the home screen'''
        proceed_flag = True
        form = MyForm(csrf_enabled=False)
        for fieldname, value in form.data.items():
            print(fieldname, value)
            if value == None:
                proceed_flag = False
        if proceed_flag:
            songname = form.name.data
            artistname = form.artist.data
            print(songname)
            print(artistname)
            return render_template('base.html', form=form)
        return render_template('base.html', form=form)
    
    @app.route('/results', methods = ['POST', 'GET'])
    def results():
        '''Returns a prediction of 10 suggested songs'''
    return app