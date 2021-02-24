# Simple Web App 3

In this app I am serving a page with three inputs, which are used to calculate an output number.
Furthermore this repo is extended with code to run pytest to test the logic.

To run the web app, run the code <code>make poetry-run-app</code>, then connect from browser on http://localhost:5000/
To run the test suite, run the code <code>make poetry-test-app</code>


## Notes

**Using flask to run "Hello World"**
* Good article with good practice: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

**Python imports with Poetry**
* Update packages variable in pyproject.toml to reflect additional package imports for pythonpath
* Using Namespace package vs regular packages: https://stackoverflow.com/a/48804718
* Using relative path for imports: https://stackoverflow.com/a/28392732

**Getting Pylance to work in vscode**
* Ensuring vs code picks up venv interpreter: https://stackoverflow.com/a/59706048 (add "~/.venv" to the settings)
