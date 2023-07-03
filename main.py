# import website package 
# from this python package 'website' import the function 'create_app'
from website import create_app

app = create_app()

# only if we run this file, not if we import this file.
# This is a pre-caution. if we import main.py somewhere else and we didn't have this line of code you could run the webserver outside of this file.
if __name__ == '__main__':
    # run flask application
    # rerun webserver if python code is changed, turn off before production.
    app.run(debug = True)
    
    