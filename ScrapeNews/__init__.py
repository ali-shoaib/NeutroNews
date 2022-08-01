from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///NewsScrapping.db'
db = SQLAlchemy(app)

from ScrapeNews import routes