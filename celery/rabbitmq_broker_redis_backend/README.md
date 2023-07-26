## Disclaimer
RabbitMQ was giving me lots of trouble running directly on my computer so I decided
to use a container to run it instead. I used two docker compose files (although you 
could certainly use just one) so I could easily see the output of the celery worker 
in a separate terminal. 

## Instructions
1. Follow the installation instructions from the README in the root directory
1. Navigate inside **rabbitmq_broker_redis_backend** directory
1. Execute `docker-compose -f docker-compose-queue.yaml up --build`
1. Open a new terminal and navigate inside **rabbitmq_broker_redis_backend** directory
1. Execute `docker-compose -f docker-compose-worker.yaml up --build`
1. Open a new terminal and navigate inside **rabbitmq_broker_redis_backend** directory
1. Execute `python3 queue_task.py`

If everything went correctly, you should see the reversed string of "celery example" ("elpmaxe yrelec") printed to your terminal after ~5 seconds. If you receive a timeout error, something is wrong. In addition, looking at the terminal running celery you should see some text similar to: 
```
rabbitmq_broker_redis_backend-celery-worker-1  | [2023-07-15 15:11:54,395: INFO/MainProcess] Task tasks.reverse[5e07c1c9-2427-42e8-b4cf-9a4856080750] received
rabbitmq_broker_redis_backend-celery-worker-1  | [2023-07-15 15:11:59,442: INFO/ForkPoolWorker-2] Task tasks.reverse[5e07c1c9-2427-42e8-b4cf-9a4856080750] succeeded in 5.0293400430000474s: 'elpmaxe yrelec'
```

