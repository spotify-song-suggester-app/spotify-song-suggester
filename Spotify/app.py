'''Main app/routing file for Spotify search app'''


import numpy as np
from flask import Flask, render_template, request, redirect
from os import getenv
from .models import DB
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

    app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'spotify_db.sqlite3' 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/', methods = ['POST', 'GET'])
    def root():
        '''At end point '/' this is the home screen'''
        #creates SQLite3 DB, and creates conn/curs for SQLite3
        conn, curs = create_table()
        print('SQL table created')
        #connects to PGSql DB, and creates cursor for it
        pg_connection = pg_conn(DBNAME, USER, PASSWORD, HOST)
        pg_curs = create_cursor(pg_connection)
        print('connecting to PG worked')
        # Create songs table in PG
        execute_q(pg_curs, CREATE_PG_TABLE, reading=False)
        print('table creation worked')
        # pulls all rows from SQLite db
        song_list = execute_q(curs, all_rows)
        print('song_list creation worked')
        # Add song_list to PGDB
        add_songs(pg_curs, song_list)
        pg_conn.commit()
        return render_template('base.html')
    
    @app.route('/results', methods = ['POST', 'GET'])
    def results():
        '''Returns a prediction of 10 suggested songs'''

        conn, curs = create_table()

        if request.method == 'POST':
            songname = request.form.get('search')
            print(songname)
            #artistname = form.artist.data
            #print(artistname)
            query = execute_q(curs, search_songs(songname.lower()))
            query = np.array(query)

            X_scaled = preprocess(query.reshape(-1, 1))

            print(X_scaled.shape)

            X_reduced = PCA(X_scaled.reshape(1, -1))

            songs = predict(X_reduced)

        return str(songs)

    
    return app