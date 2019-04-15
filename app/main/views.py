from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources, get_articles, search_source
from ..models import Source, Article


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

     #Getting news Sources
    general_sources = get_sources('general')
    entertainment_sources = get_sources('entertainment')
    business_sources = get_sources('business')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    health_sources = get_sources('health')
    science_sources = get_sources('science')

    title = 'Get the latest news!'
    search_source = request.args.get('source_query')

    if search_source:
        return redirect(url_for('.search',source_name=search_source))
    else:
        return render_template('index.html', title = title, general = general_sources,entertainment = entertainment_sources, business = business_sources, sports = sports_sources, technology = technology_sources, health = health_sources, science = science_sources)

   

@main.route('/articles/<id>')
def articles(id):
    '''
    View Source page function that returns news source details and its data
    '''

    source = get_articles(id)
    # title = f'{source.title}'
    return render_template('articles.html',id = id, source = source)

# @app.route('/source/<int:id>')
# def source(id):
#     '''
#     View Source page function that returns news source details and its data
#     '''

#     source = get_source(id)
#     title = f'{source.title}'
#     return render_template('source.html', title = title, source = source)


@main.route('/search/<source_name>')
def search(source_name):
    '''
    View function to display the search results
    '''
    source_name_list = source_name.split(" ")
    source_name_format = "+".join(source_name_list)
    searched_sources = search_source(source_name_format)
    title = f'search results for {source_name}'
    return render_template('search.html',sources = searched_sources)