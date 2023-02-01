from flask import Flask
from flask_fontawesome import FontAwesome
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
fa = FontAwesome(app)
migrate = Migrate(app, db)
app.config.from_object('config')

from app.service import control


