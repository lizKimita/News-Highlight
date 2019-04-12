from flask import render_template
from app import app
from .request import get_sources, get_articles

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
    health_sources = get_sources('health')
    science_sources = get_sources('science')

    title = 'Get the latest news!'
    return render_template('index.html', title = title, general = general_sources,entertainment = entertainment_sources, business = business_sources, sports = sports_sources, technology = technology_sources, health = health_sources, science = science_sources)

   

@app.route('/articles/<int:source_id>')
def source(source_id):
    '''
    View Source page function that returns news source details and its data
    '''

    articles = get_articles(source_id)
    title = f'{source_id}|All Articles'
    return render_template('articles.html', title = title, id = source_id, article = articles)