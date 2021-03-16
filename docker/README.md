# Running apps in Docker

This folder includes two apps to be run inside DOcker.

## app1
This app accomplishes:
* restructuring the code into packages under src folder (requires pythonpath reference, but updating pyproject.toml)
* running the flask app from a package, instead of file (ie. "flaskapp" -- required main file)
* setting up Dockerfile to create image and run the app in a container

## app2
This app accomplishes:
* redefine application as two services in different containers (redis + app3)
* introduce docker-compose to start services together and map services automatically
