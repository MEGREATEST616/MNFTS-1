from flask import *
from sqlalchemy import or_
from . import main
from .forms import EditProfileForm, CommentForm, AddForm, EditMovieForm
from flask_login import login_required, current_user
from .. import db
from ..models import User


@main.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")