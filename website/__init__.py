# create flask application
from flask import Flask

def create_app():
    app = Flask(__name__) # name of file that was ran
    app.config['SECRET_KEY'] = 'po1sas2zsaz3sxzwqa4oijre' # SECURE COOKIES AND SESSION 
    
    # import our views
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    
    return app

