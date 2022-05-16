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
    
    with urllib.request.urlopen(base_url) as url:
        get_quotes_data = url.read()
        get_quote = json.loads(get_quotes_data)
        quote_results_list = get_quote;
        quote_results = process_results(quote_results_list)
        
        
    return quote_results
    
    
def process_results(quote_list):
    '''
      function that process our results
    '''
    quote_result = []
    
    for quote_item in quote_list:
        author = quote_item.get('author')
        quote = quote_item.get('quote')
        link = quote_item.get('permalink')
        quote_object = Quote_source(author,quote,link)
        
        quote_result.append(quote_object)
        
    return quote_result
        