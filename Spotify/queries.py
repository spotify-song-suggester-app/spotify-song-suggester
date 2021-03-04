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
total_rows = '''
SELECT COUNT(*)
FROM Songs
'''
