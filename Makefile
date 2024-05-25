setup:
	pip install -r requirements/requirements.dev
	pre-commit install

pytest:
	pytest --cov-report term --cov=app ./tests

pre-commit:
	pre-commit run --all-files

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
	find . | grep -E ".pytest_cache" | xargs rm -rf
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf
	rm -rf .coverage*
