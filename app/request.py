from app import app
import urllib.request,json
from .models import source

Source = source.Source

# Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain the source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []

    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        category = source_item.get('category')
        country = source_item.get('country')
        url = source_item.get('url')

        if url:
            source_object = Source(id, name, description, category, country, url)
            source_results.append(source_object)

    return source_results

def get_articles(source_id):
    '''
    Function that gets the articles data for each source id
    '''
    get_source_details_url = base_url.format(source_id,api_key)

    with urllib.request.urlopen(get_source_details_url) as url:
        articles_details_data = url.read()
        articles_details_response = json.loads(articles_details_data)

        articles_object = None

        if articles_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)

    return movie_object