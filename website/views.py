# Store standard routes/views for our users.
from flask import Blueprint

#blueprint of our applications. a way to separate our views

views = Blueprint('views', __name__)

#decorator 
@views.route('/')
def home():
    return "<h1>Test</h1>"

