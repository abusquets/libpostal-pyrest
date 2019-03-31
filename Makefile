build:
	docker build -t libpostal-pyrest-docker .

run:
	docker run --rm -p8001:8001 -ti libpostal-pyrest-docker
