import unittest
from app.models import Quote_source

class QuoteSourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the quote_source class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Quote_source("Unkown","Necessity is the mother of invention")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Quote_source))