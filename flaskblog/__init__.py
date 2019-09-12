###this is the package to enable us to divide the program...
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


###to run FLASK WEB SERVER:
#execute command to register as env variables. second one refreshes the server live
#export FLASK_APP=flaskblog.py
#export FLASK_DEBUG=1
#flask run
## add name == main and run the file directly =  works better.


app = Flask(__name__)
###generate key with python secrets module
app.config['SECRET_KEY'] = 'be55d207f7a71bdaf2d529cbb90d4f3a'
###this creates a DB in local directory. Run db.create_all() in terminal to create the DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
##this creates an instance
db = SQLAlchemy(app)

from flaskblog import routes