from flask import Flask
from flask_cors import CORS
from celery import Celery
import os

app = Flask(__name__)
CORS(app)
app.config['CELERY_MESSAGE_BROKER_URL'] = os.getenv("CELERY_MESSAGE_BROKER_URL")
app.config['CELERY_DATABASE_URL'] = os.getenv("CELERY_DATABASE_URL")
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['CELERY_TASK_TIME_LIMIT'] = 600

celery = Celery(app.import_name,
    backend=app.config['CELERY_DATABASE_URL'],
    broker=app.config['CELERY_MESSAGE_BROKER_URL'])
celery.conf.update(app.config)
