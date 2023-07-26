## Prerequisites
- You shoulder have working knowledge of Docker and Kubernetes 
- I highly recommend this [Udemy Course by Stephen Grider](https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/) for learning both from scratch


## Implement a task queue in Kubernetes
- Learn how to implement a task queue in Kubernetes by following this tutorial from 2021: [Scaling Celery workers with RabbitMQ on Kubernetes Blog Tutorial](https://learnk8s.io/scaling-celery-rabbitmq-kubernetes)
    
- Here are my [corrections and updates](https://clipsai.notion.site/Scaling-Celery-workers-with-RabbitMQ-on-Kubernetes-4d52aa54c1f64babb60f91fa86ff2b1f?pvs=4) as well as [my GitHub repo](https://github.com/bensmidt/k8s/tree/main/task-queue/original_tutorial_updates_corrections) containing those updates and corrections (2023)


## Use Redis instead of RabbitMQ and Postgres
- If you'd like to use Redis (for both the broker and/or database), you can easily do so by 
swapping out the Kubernetes containers and URLs used by Celery, which I've done [here](https://github.com/bensmidt/k8s/tree/main/task-queue/redis/README.md) 