from flask import render_template
from app import app
from .request import get_sources

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

     #Getting General news Sources
    general_sources = get_sources('general')
    entertainment_sources = get_sources('entertainment')
    business_sources = get_sources('business')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')

    title = 'Home - Be on the know by catching up with the latest new here!'
    return render_template('index.html', title = title, general = general_sources,entertainment = entertainment_sources, business = business_sources, sports = sports_sources, technology = technology_sources)

   

@app.route('/source/<int:source_id>')
def source(source_id):
    '''
    View Source page function that returns news source details and its data
    '''
    return render_template('source.html', id = source_id)