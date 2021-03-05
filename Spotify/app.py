'''Main app/routing file for Spotify search app'''


import numpy as np
from flask import Flask, render_template, request, redirect
from os import getenv
from .models import *
from .cleandf import *
from .forms import MyForm
from .queries import *
from .predict import *


DBNAME = 'qrcbzxhn'
USER = 'qrcbzxhn'
PASSWORD = 'JTbDJaM6Pr9hSynJ1ZgZwNpWEf04DS8Y '
HOST = 'isilo.db.elephantsql.com'

def create_app():
    '''Create flask app'''
    app = Flask(__name__)

    #app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///spotify_db.sqlite3' 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        '''At end point '/' this is the home screen'''
        # Creates SQLite3 DB, and creates conn/curs for SQLite3
        conn, curs = create_table()
        # print('SQL table created')
        # Pulls all rows from sqlite db
        # song_list = execute_q(curs, all_rows)
        # print('song_list creation worked')
        # Add_songs(pg_curs, song_list)
        # add_songs_SQLA(song_list)
        #pg_conn.commit()
        return render_template('base.html')

    @app.route('/results', methods=['POST'])
    def results():
        '''Returns a prediction of 10 suggested songs'''

        conn, curs = create_table()

        if request.method == 'POST':
            songname = request.form.get('search')
        
            query = execute_q(curs, search_songs(songname.lower()))
            query = np.array(query)

            X_scaled = preprocess(query.reshape(-1, 1))

            print(X_scaled.shape)

            X_reduced = PCA(X_scaled.reshape(1, -1))

            songs = predict(X_reduced)

            results = []

            for i in songs:
                result = execute_q(curs, search_rows(i))
                results.append(result)


        return render_template('results.html', results=results)

    
    return app