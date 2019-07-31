from flask import Flask
from flask_mongoengine import MongoEngine
app = Flask(__name__)

app.config.from_object('config')

db = MongoEngine(app) #实例化mongoengine

from app import views, models