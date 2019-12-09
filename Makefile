push:
	gcloud builds submit --tag gcr.io/<project>/locust-http-perf-tester:latest docker

deploy:
	kubectl apply -f kubernetes/

clean:
	kubectl delete svc locust-master
	kubectl delete deploy locust-master
	kubectl delete deploy locust-worker
