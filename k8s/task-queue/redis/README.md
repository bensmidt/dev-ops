## Prerequisites
- To use this repo, you should've already followed this tutorial [Scaling Celery workers with RabbitMQ on Kubernetes Blog Tutorial](https://github.com/bensmidt/k8s/tree/main/task-queue)

## Changes
- Utilize `Redis` instead of `PostgresSQL` as the database
- Utilize `Redis` instead of `RabbitMQ` as the message broker
- Added an nginx ingress controller as the entry point to the cluster
- Heavily edited the naming conventions used in the kubernetes (k8s) yaml files from 
the previous repository


## Nginx Ingress Controller
- To use the nginx ingress controller, follow this [link](https://kubernetes.github.io/ingress-nginx/deploy/#quick-start) and run the YAML manifest option
    - Ex: `kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.0/deploy/static/provider/cloud/deploy.yaml`
- Make sure to apply the `ingress_service.yaml` file to your cluster
- Access the cluster from http://localhost (you DO NOT need to setup port forwarding)
    - Examples
        - `curl -X POST http://localhost/report`
        - `curl http://localhost/report/<report-id>`
