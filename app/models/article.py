class Article:
    '''
    Article class to define the Article Objects
    '''

    def __init__(self, source_id, source_name, author, title, description, urlToImage, publishedAt, url ):
        self.source_id = source_id
        self.source_name = source_name
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.url = url

        (5467,'BBC Kenya','Kevin Kittony','Big change in Kenya','get the tips to making big changes','https://newsapi.org/v2/image','2019-04-12,', 'https://newsapi.org/v2/bigchanges')