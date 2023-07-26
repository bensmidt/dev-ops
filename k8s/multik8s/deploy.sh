docker build -t benjaminsmidt/multi-client:latest -t benjaminsmidt/multi-client:$SHA -f ./client/Dockerfile ./client
docker build -t benjaminsmidt/multi-server:latest -t benjaminsmidt/multi-server:$SHA -f ./server/Dockerfile ./server
docker build -t benjaminsmidt/multi-worker:latest -t benjaminsmidt/multi-worker:$SHA -f ./worker/Dockerfile ./worker
# should already be logged into docker
docker push benjaminsmidt/multi-client:latest
docker push benjaminsmidt/multi-server:latest
docker push benjaminsmidt/multi-worker:latest

docker push benjaminsmidt/multi-client:$SHA
docker push benjaminsmidt/multi-server:$SHA
docker push benjaminsmidt/multi-worker:$SHA
# should already be connected to kubectl cluster 
kubectl apply -f k8s
# ensure we do latest image for each deployment 
kubectl set image deployments/client-deployment client=benjaminsmidt/multi-client:$SHA
kubectl set image deployments/server-deployment server=benjaminsmidt/multi-server:$SHA
kubectl set image deployments/worker-deployment worker=benjaminsmidt/multi-worker:$SHA
