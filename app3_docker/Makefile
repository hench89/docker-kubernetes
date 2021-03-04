APP_NAME=mycontainer
PORT=5000

poetry-run:
	export FLASK_APP=flaskapp; \
	poetry run flask run

poetry-test:
	poetry run pytest

docker-build: Dockerfile
	docker build -t $(APP_NAME) .

docker-run: docker-build
	docker run --init -it -p=$(PORT):$(PORT) $(APP_NAME)

docker-test:
	docker run $(APP_NAME) poetry run pytest

docker-bash:
	docker run --rm -it --entrypoint bash $(APP_NAME)
