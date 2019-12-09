# K8s load testing client using Locust

## Run locally

`docker-compose up`

Access the console on localhost:8089

## Remove local 

`docker-compose down --rmi all -v --remove-orphans`

## Run on GCP
- Build the Docker image and store it in your project's container registry:
    `make push`

- Create 4 node GKE cluster


- Deploy:
  `make deploy`


## Cleanup
`make clean`

## HPA
`kubectl autoscale deployment feathers --min=1 --max=10 --cpu-percent=80`
