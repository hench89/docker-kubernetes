# Running apps in Docker

This folder includes two apps to be run inside Docker.

## App 1: Hello world
This app accomplishes:
* restructuring the code into packages under src folder (requires pythonpath reference, but updating pyproject.toml)
* running the flask app from a package, instead of file (ie. "flaskapp" -- required main file)
* setting up Dockerfile to create image and run the app in a container

## App 2: Building a multi-container app
This app accomplishes:
* redefine application as two services in different containers (redis + app3)
* introduce docker-compose to start services together and map services automatically

# References

* [Run Docker in WSL on Windows](https://kubernetes.io/blog/2020/05/21/wsl-docker-kubernetes-on-the-windows-desktop/)
* [Getting Started with Docker-compose](https://docs.docker.com/compose/gettingstarted/)
* [Multi app tutorial](https://docs.microsoft.com/en-us/visualstudio/docker/tutorials/multi-container-apps)
