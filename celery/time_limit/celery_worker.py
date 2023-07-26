from celery import Celery
from celery.exceptions import SoftTimeLimitExceeded
from time import sleep

broker_url = 'amqp://guest:guest@localhost:5672'
app = Celery('tasks', broker=broker_url)

@app.task(bind=True, soft_time_limit=1)
def sleeptask(self):
    print('Task started')
    try:
        sleep(5)
        print('Task finished')
    except SoftTimeLimitExceeded:
        print('Soft time limit exceeded!')