from app import app
import urllib.request,json
from .models import source,article

Source = source.Source
Article = article.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
articles_url = app.config["ARTICLES_BASE_URL"]


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



# def get_source(id):
#     get_source_details_url = articles_url.format(id,api_key)

#     with urllib.request.urlopen(get_source_details_url) as url:
#         source_details_data = url.read()
#         source_details_response = json.loads(source_details_data)

#         source_object = None

#         if source_details_response:
#             id = source_details_response.get('id')
#             author = source_details_response.get('author')
#             title = source_details_response.get('title')
#             description = source_details_response.get('description')
#             url = source_details_response.get('url')
#             urlToImage = source_details_response.get('urlToImage')
#             publishedAt = source_details_response.get('publishedAt')

#             source_object = Source (id,author,title,description,url,urlToImage,publishedAt)

#     return source_object


def get_articles(id):
    '''
    Function that gets the articles data for each id
    '''
    get_article_url = articles_url.format(id,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results


def process_articles(articles_list):
    '''
    Function  that processes the articles results and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain the articles details

    Returns :
        articles_results: A list of articles objects
    '''
    articles_results= []
    
    for articles_item in articles_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        if urlToImage:
            articles_object = Articles (id,author,title,description,url,urlToImage,publishedAt)
            articles_results.append(articles_object)
        
    return articles_results

def search_source(source_name):
    search_source_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(api_key,source_name)  
    with urllib.request.urlopen(search_source_url) as url:
        search_source_data = url.read()
        search_source_response = json.loads(search_source_data)

        search_source_results = None

        if search_source_response['sources']:
            search_source_list = search_source_response['sources']
            search_source_results = process_results(search_source_list)


    return search_source_results