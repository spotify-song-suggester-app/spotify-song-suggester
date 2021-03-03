def search_songs(SONGNAME):
    return f'''
        SELECT name FROM Songs
        WHERE name == \'{SONGNAME}\' 
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
