APP_NAME=multi-docker-app
APP_PORT=5000

compose-build:
	docker-compose build

compose-run: compose-build
	docker-compose up

compose-down:
	docker-compose down

docker-build: Dockerfile
	docker build -t $(APP_NAME) .

docker-run: docker-build
	docker run --init -it -p=$(APP_PORT):$(APP_PORT) $(APP_NAME)

docker-test: docker-build
	docker run $(APP_NAME) poetry run pytest

docker-bash: docker-build
	docker run --rm -it --entrypoint bash $(APP_NAME)
