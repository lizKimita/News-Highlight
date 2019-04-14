class Source:
    '''
    Source class to define the Source Objects
    '''

    def __init__(self, id, name, description, category, country, url ):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.country = country
        self.url = url
    
class Article:
    '''
    Article class to define the Article Objects
    '''

    def __init__(self, id, author, title, description, urlToImage, publishedAt, url ):
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.url = url

        (5467,'Kevin Kittony','Big change in Kenya','get the tips to making big changes','https://newsapi.org/v2/image','2019-04-12,', 'https://newsapi.org/v2/bigchanges')