from operator import ge
from flask import render_template
from . import main
from app.request import get_random_quote

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    all_quotes = get_random_quote();
    print(all_quotes)
    return render_template('index.html',all_quotes=all_quotes)