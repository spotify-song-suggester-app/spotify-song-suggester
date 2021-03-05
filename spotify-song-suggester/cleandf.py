'''Austin Francis' wrangle function and DB creation'''


import pandas as pd
import re
import numpy as np
import sqlite3
from .models import *
from .queries import *


def create_table():
    '''Convert CSV to SQLite3 DB'''
    conn, curs = sl_conn(sqlite_db='spotify_db.sqlite3')
    df = wrangle()
    df.to_sql('Songs', con=conn, if_exists='replace')
    #results = execute_q(curs=curs, query=total_rows)

    return conn, curs



def wrangle():
    '''Wrangle function from Austin to clean Spotify Song data'''
    # filename='D:\Lambda\Buildweek\spotify-song-suggester\Spotify\data.csv'
    filename='data.csv'
    # read csv
    df = pd.read_csv(filename, parse_dates=['release_date'], index_col='id')

    # Replace brackets in artists column to avoid PGSql conflicts
    df['artists'] = df['artists'].str.replace('[','')
    df['artists'] = df['artists'].str.replace(']','')
    df['artists'] = df['artists'].str.replace("'", '')

    # convert duration from ms to min
    df['duration_min'] = df['duration_ms'] / 60000
    df['duration_min'] = df['duration_min'].round(2)

    # lower-case song name
    df['name'] = df['name'].str.lower()
    # strip ' from song name 
    df['name'] = df['name'].str.replace("'", "")
    # drop duplicate values
    df.drop_duplicates(inplace=True)

    # drop duration_ms and release_date
    df.drop('duration_ms', axis=1, inplace=True)
    df.drop('release_date', axis=1, inplace=True)

    return df


def sl_conn(sqlite_db):
    '''connect to sqlite db'''
    conn = sqlite3.connect(sqlite_db)
    curs = conn.cursor()
    return conn, curs


def execute_q(curs, query, reading=True):
    '''execute query with connection'''
    curs.execute(query)
    if reading:
        results = curs.fetchall()
        return results
    return 'This statment worked'

def pg_conn(dbname, user, password, host):
    '''returns pg connection'''
    pg_conn = psycopg2.connect(dbname=DBNAME, user=USER,
                                password=PASSWORD, host=HOST)
    return pg_conn

def create_cursor(conn):
    '''returns cursor'''
    curs = conn.cursor()
    return curs

def add_songs(pg_curs, song_list):
    '''Insert song_list into PGSQL DB table'''

    for song in song_list:
        pg_curs.execute(INSERT_PG.format(song))
    
def add_songs_SQLA(song_list):
    '''Add all rows from sqlite db into SQLAlchemy Songs class'''
    DB.create_all()
    for song in song_list:
        song = Songs(id = song[0],
                    acousticness = song[1],
                    artists = song[2],
                    danceability = song[3],
                    energy = song[4],
                    explicit = song[5],
                    instrumentalness = song[6],
                    key = song[7],
                    liveness = song[8],
                    loudness = song[9],
                    mode = song[10],
                    name = song[11],
                    popularity = song[12],
                    speechiness = song[13],
                    tempo = song[14],
                    valence = song[15],
                    year = song[16],
                    duration_min = song[17])
        DB.session.add(song)
    DB.session.commit()
