from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    return render_template('index.html')

@app.route('/source/<int:source_id>')
def source(source_id):
    '''
    View Source page function that returns news source details and its data
    '''
    return render_template('source.html', id = source_id)