'''Main app/routing file for Spotify search app'''

from flask import Flask, render_template, request



def create_app():
    '''Create flask app'''
    app = Flask(__name__)

    #app.config['SQLALCHEMY_DATABASE_URI'] = 'spotify_db.sqlite3' 
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #DB.init_app(app)
    
    @app.route('/')
    def root():
        '''At end point '/' this is the home screen'''
        return 'this is a home page'
    
    return app
