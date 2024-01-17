## Create a simple flask application.
from flask import Flask
##create flask app
app=Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/welcome')
def welcome():
    return 'welcome to the flask tutorial'


if __name__=='__main__':
    app.run(debug=True)