from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField, StringField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')
    

class BlogForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    blog = TextAreaField('Blog', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
    
class CommentsForm(FlaskForm):
    comment_detail = TextAreaField('Leave a Comment', validators=[DataRequired()])
    submit = SubmitField('Submit')
    