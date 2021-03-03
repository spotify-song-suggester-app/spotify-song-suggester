'''Main app/routing file for Spotify search app'''

from flask import Flask, render_template, request, redirect
from os import getenv
from .models import DB
from .cleandf import *
from .forms import MyForm
from .queries import *

def create_app():
    '''Create flask app'''
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'spotify_db.sqlite3' 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    SONGNAME = ''
    ARTISTNAME = ''

    @app.route('/', methods = ['POST', 'GET'])
    def root():
        '''At end point '/' this is the home screen'''
        proceed_flag = True
        form = MyForm(meta={'csrf': False})

        for fieldname, value in form.data.items():
            if not value:
                proceed_flag = False
        if proceed_flag:
            SONGNAME = form.name.data
            ARTISTNAME = form.artist.data
        
        return render_template('base.html', form=form)
    
    @app.route('/results', methods = ['POST', 'GET'])
    def results():
        '''Returns a prediction of 10 suggested songs'''
        conn, curs = create_table()
            
        q = execute_q(curs, search_songs(SONGNAME))
        
        return str(q)
    
    return app