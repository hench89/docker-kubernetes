# Simple Web App

In this project, I am running a simple app to parse Hello World on http.

## Poetry
The project is using poetry as a dependency- and package manager.
To run the project you need to have Python and Poetry installed.
To setup the project on your local machine, run command <code>poetry install</code>.


## Running on Debian

When running poetry on debian, it is important that pip is installed and updated for python2 and python3.
The following guide is great: https://linuxize.com/post/how-to-install-pip-on-debian-9/#install-pip-for-python-2

To run the web app, run the code <code>make poetry-run-app</code>, then connect from browser on http://localhost:5000/
