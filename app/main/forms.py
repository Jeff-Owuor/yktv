from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField, StringField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')
    

class BlogForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    blog = TextAreaField('Blog', validators=[DataRequired()])
    author = StringField('Author',validators=[DataRequired()])
    submit = SubmitField('Submit')
    
    