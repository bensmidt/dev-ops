from celery import Celery
from redis import Redis
from time import sleep

server = Celery(
    'tasks', # name of the celery app
    broker='redis://localhost:6379/1', 
    backend='redis://localhost:6379/0'
)
server.conf.task_track_started = True

@server.task
def reverse(text: str): 
    sleep(5)
    return text[::-1]
