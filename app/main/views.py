from operator import ge
from flask import render_template,request,redirect,url_for,abort
from . import main
from app.request import get_random_quote
from .forms import BlogForm
from ..models import User,Blogs,Votes,Comment
from flask_login import login_required, current_user

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    blogs = Blogs.query.all()
    all_quotes = get_random_quote()
    return render_template('index.html',all_quotes=all_quotes,blogs = blogs)

@main.route('/post')
def post():
    '''
      function for displaying the blog post
    '''
    form = BlogForm()
    if form.validate_on_submit():
        blog = form.blog.data
        author = form.author.data
        title = form.tile.data
        user_id = current_user._get_current_object().id
        new_blog_dict = Blogs(blog = blog,user_id=user_id,author = author, title = title)
        new_blog_dict.save_blog()
        return redirect(url_for('main.index'))
        
    return render_template('post.html')

@main.route('/add')
def add():
    
    return render_template('add.html')