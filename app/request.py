from email.quoprimime import quote
import urllib.request,json
from .models import Quote_source;

base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['RANDOM_QUOTE_URL']

def get_random_quote():
    '''
      Function that gets the random quotes from the random qoute api
    '''
    quote_object = None
    with urllib.request.urlopen(base_url) as url:
        get_quotes_data = url.read()
        get_quote = json.loads(get_quotes_data)
        
        author = get_quote.get('author')
        quote = get_quote.get('quote')
        quote_object = Quote_source(author,quote)
        
    return quote_object
    