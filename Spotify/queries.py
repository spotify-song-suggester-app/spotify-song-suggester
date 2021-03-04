def search_songs(SONGNAME):
    print(SONGNAME)
    return f'''
    SELECT acousticness,danceability,duration_min,energy,explicit,instrumentalness,key,liveness,loudness,mode,popularity,speechiness,tempo,valence,year  
    FROM Songs
    WHERE name ==  "{SONGNAME}"
    '''

def search_artists(ARTISTNAME):
    return f'''
        Select artists FROM Songs
        WHERE artists == {ARTISTNAME} 
    '''

# Test sql command to see if SQLite3DB works
all_rows = '''
    SELECT *
    FROM Songs
    '''

CREATE_PG_TABLE = '''
CREATE TABLE IF NOT EXISTS Songs (
    id VARCHAR(50),
    acousticness FLOAT(50),
    artists VARCHAR(50),
    danceability FLOAT(50),
    duration_min FLOAT(5),
    energy FLOAT(50),
    explicit SMALLINT,
    instrumentalness FLOAT(50),
    key SMALLINT,
    liveness FLOAT(50),
    loudness FLOAT(50),
    mode SMALLINT,
    name VARCHAR(50),
    popularity SMALLINT,
    speechiness FLOAT(50),
    tempo FLOAT(20),
    valence FLOAT(20),
    year SMALLINT
);
'''

INSERT_PG = '''
INSERT INTO Songs(
    id,
    acousticness,
    artists,
    danceability,
    duration_min,
    energy,
    explicit,
    instrumentalness,
    key,
    liveness,
    loudness,
    mode,
    name,
    popularity,
    speechiness,
    tempo,
    valence,
    year
    ) VALUES {};
'''