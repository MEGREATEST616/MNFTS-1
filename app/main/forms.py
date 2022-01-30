from flask_wtf import Form, FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.fields import DateField
from wtforms.validators import DataRequired, URL





class EditProfileForm(FlaskForm):
    name = StringField('Real name')
    location = StringField('Location')
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    body = TextAreaField("What's on your mind?", validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddForm(FlaskForm):
    title = StringField('Movie Title')
    year = IntegerField('Year')
    length = IntegerField('Length')
    description = TextAreaField('Description')
    url = StringField('URL')
    submit = SubmitField('Submit')

class EditMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    length = IntegerField('Length', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    url = StringField('URL', validators=[DataRequired()])
    submit = SubmitField('Submit')
