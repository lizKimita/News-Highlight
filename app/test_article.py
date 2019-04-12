import unittest
from models import article
Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article(5467,'BBC Kenya','Kevin Kittony','Big change in Kenya','get the tips to making big changes','2019-04-12,', 'https://newsapi.org/v2/bigchanges')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()