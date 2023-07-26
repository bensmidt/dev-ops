from app.app import celery
from flask import request
import time
import random

@celery.task(name="report", acks_late=True)
def report():
    print("Generating report")
    time.sleep(300)
    return {"state":"completed"}
