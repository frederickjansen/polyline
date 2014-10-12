setup-base-dependencies:
	pip install --quiet --requirement=requirements/base.txt

setup-test-dependencies:
	pip install --quiet --requirement=requirements/test.txt

pep8-tests:
	flake8 --ignore=E128,E501 polyline

unit-tests:
	nosetests

reqs: setup-base-dependencies setup-test-dependencies

test: pep8-tests unit-tests
