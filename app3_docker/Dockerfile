# select base image
FROM python:3.7-slim
WORKDIR '/app'

# make sure to install and setup poetry
RUN pip3 install poetry
RUN poetry config virtualenvs.create false

# install project dependencies in image
RUN mkdir -p /app/src
WORKDIR /app
COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-root

# copy source code and install again
COPY src /app/src
RUN poetry install

# run code
ENV FLASK_APP=flaskapp
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
