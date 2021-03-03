'''Austin Francis' wrangle function and DB creation'''


import pandas as pd
import re
import numpy as np
import sqlite3
from .models import DB

def create_table():
    '''Convert CSV to SQLite3 DB'''
    conn, curs = sl_conn(sqlite_db='spotify_db.sqlite3')
    df = wrangle()
    df.to_sql('Songs', con=conn, if_exists='replace')
    results = execute_q(curs=curs, query=total_rows)
    print(results[:10])


# Wrangle function from Austin to clean Spotify Song data
def wrangle(filename='../data.csv'):
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


def sl_conn(sqlite_db):
    '''connect to sqlite db'''
    conn = sqlite3.connect(sqlite_db)
    curs = conn.cursor()
    return conn, curs


def execute_q(curs, query):
    '''execute query with connection'''
    results = curs.execute(query).fetchall()
    return results

<<<<<<< HEAD
# Test sql command to see if SQLite3DB works
=======

>>>>>>> c1e672db1ea8a1cfca816114eeef2a9ea90ee39b
total_rows = '''
SELECT COUNT(*)
FROM Songs
'''
<<<<<<< HEAD
# Convert SQLite3DB into SQLAlchemy class in .models
def add_song(song):
    '''Takes song from sqlite3db and inserts into Song Class'''
    for song in 


if __name__ == '__main__':
    conn, curs = sl_conn(sqlite_db='spotify_db.sqlite3')
    df = wrangle()
    df.to_sql('Songs', con=conn)
    results = execute_q(curs=curs, query=total_rows)
    print(results[:10])
=======
>>>>>>> c1e672db1ea8a1cfca816114eeef2a9ea90ee39b