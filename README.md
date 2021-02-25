# Simple Web App

In this project, I am creating a few a simple apps to learn about python and devops.
The different apps touch basic concepts of working with:
* git/github
* poetry package manager
* debian linux distribution (manage and run code)
* makefile
* docker
* kubernetes (minikube/cubectl/cubectx)
* ci/cd (testing and deployment)

## app1
The first app accomplishes:
* manage python virtualenvironment and dependencies with Poetry
* setting up a basic flask app that prints hello world
* setting up makefile to document different ways of running the ap

## app2
The second app accomplishes:
* extending flask app with a simple page to (1) read inputs (2) calculate a result based on some logic (3) return result to user
* adding a few test cases to run against the logic

## app3
The third app accomplishes:
* restructuring the code into packages under src folder (requires pythonpath reference, but updating pyproject.toml)
* running the flask app from a package, instead of file (ie. "flaskapp" -- required main file)
* setting up Dockerfile to create image and run the app in a container

## app4
The fourth app accomplishes:
* redefine application as two services in different containers (redis + app3)
* introduce docker-compose to start services together and map services automatically

# Resources

## Configuration

* VSCode: To hide pycache files/folders: https://m3lles.medium.com/how-to-hide-unwanted-folders-and-files-in-visual-studio-code-2bb0f39c4251
* VSCode: Pickup correct venv interpreter: https://stackoverflow.com/a/59706048 (add "~/.venv" to the settings)
* Debian: Make sure to have pip installed and updated: https://linuxize.com/post/how-to-install-pip-on-debian-9/#install-pip-for-python-2
* Debian: Sometimes docker service wont start https://github.com/docker/compose/issues/7495 (update variable in ~/.docker/config.json)

## Articles

* Flask: Making a simple Hello World app: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
* Python: Using relative path for python imports: https://stackoverflow.com/a/28392732
* Python: Using Namespace package vs regular packages: https://stackoverflow.com/a/48804718
* Poetry: Add additional package references to pythonpath: https://python-poetry.org/docs/pyproject/#packages
* Docker-compose: https://docs.microsoft.com/en-us/visualstudio/docker/tutorials/multi-container-apps
* Docker-compose: https://docs.docker.com/compose/gettingstarted/
