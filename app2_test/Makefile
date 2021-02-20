poetry-run-app:
	export FLASK_APP=$(PWD)/src/routes.py; \
	poetry run python -m flask run

poetry-test-app:
	export PYTHONPATH=$(PWD); \
	poetry run pytest
