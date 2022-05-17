
from operator import ge
from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .. import db,photos
from app.request import get_random_quote
from .forms import BlogForm,UpdateProfile,CommentsForm
from ..models import User,Blogs,Votes,Comment
from flask_login import login_required, current_user
import os


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    blogs = Blogs.query.all()
    all_quotes = get_random_quote()
    return render_template('index.html',all_quotes=all_quotes,blogs = blogs)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/post',methods = ['POST','GET'])
def new_post():
    '''
      function for displaying the blog post
    '''
    form = BlogForm()
    if form.validate_on_submit():
        blog = form.blog.data
        title = form.title.data
        user_id = current_user._get_current_object().id
        new_blog_dict = Blogs(blog = blog,user_id=user_id, title = title)
        new_blog_dict.save_blog()
        return redirect(url_for('main.index'))
        
    return render_template('post.html', form = form)

@main.route('/comments/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):
    blog = Blogs.query.filter_by(id=id).first()
    form = CommentsForm()
    if blog is None:
        abort(404)
        
    
    if form.validate_on_submit():
        comments = form.comment_detail.data
        user_id = current_user._get_current_object().id
        new_comment = Comment( comment=comments, user_id = user_id, blog_id = blog.id )
        new_comment.save_comment()
        return redirect(url_for('.add_pitch', id=blog.id ))
    return render_template('comments.html',form=form)



@main.route('/blog/<blogId>/delete', methods = ['POST'])
def delete_blog(blogId):
    blog = Blogs.query.get(blogId)
    if blog.user != current_user:
        abort(403)
    blog.delete_blog()

    flash("Blog Deleted")
    return redirect(url_for('.index'))


@main.route('/a_pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def add_pitch(id):
    blogs = Blogs.query.get(id)
    
    if blogs is None:
        abort(404)
    
    comment = Comment.get_comments(id)
    count_likes = Votes.query.filter_by(blog_id=id, vote=1).all()
    count_dislikes = Votes.query.filter_by(blog_id=id, vote=2).all()
    return render_template('add_pitch.html', blogs = blogs, comment = comment, count_likes=len(count_likes), count_dislikes=len(count_dislikes))

@main.route('/blog/upvote/<int:id>&<int:vote_type>')
@login_required
def upvote(id,vote_type):
    votes = Votes.query.filter_by(user_id=current_user.id).all()
    print(f'The new vote is {votes}')
    to_str=f'{vote_type}:{current_user.id}:{id}'
    print(f'The current vote is {to_str}')

    if not votes:
        new_vote = Votes(vote=vote_type, user_id=current_user.id, blog_id=id)
        new_vote.save_vote()
        print('YOU HAVE  NEW VOTE')

    for vote in votes:
        if f'{vote}' == to_str:
            print('YOU CANNOT VOTE MORE THAN ONCE')
            break
        else:   
            new_vote = Votes(vote=vote_type, user_id=current_user.id, blog_id=id)
            new_vote.save_vote()
            print('YOU HAVE VOTED')
            break
    return redirect(url_for('.add_pitch', id=id))   
    
