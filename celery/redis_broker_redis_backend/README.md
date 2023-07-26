## Instructions
1. Follow the installation instructions from the README in the root directory
1. Navigate inside **redis_broker_redis_backend** directory
1. Execute `docker-compose up --build`
1. Open a new terminal and navigate inside **redis_broker_redis_backend** directory
1. Execute `celery -A tasks worker --loglevel=info`
1. Open a new terminal and navigate inside **redis_broker_redis_backend** directory
1. Execute `python3 queue_task.py`

If everything went correctly, you should see the reversed string of "celery example" ("elpmaxe yrelec") printed to your terminal after ~5 seconds. If you receive a timeout error, something is wrong. In addition, looking at the terminal running celery you should see some text similar to: 
```
[2023-06-02 07:28:00,665: INFO/MainProcess] Task tasks.reverse[07b4d654-0207-40eb-a6b8-4000dc4ed0cc] received
[2023-06-02 07:28:05,705: INFO/ForkPoolWorker-8] Task tasks.reverse[07b4d654-0207-40eb-a6b8-4000dc4ed0cc] succeeded in 5.034314874999836s: 'elpmaxe yrelec'
```

