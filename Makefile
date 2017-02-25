.PHONY: clean release dist install

clean:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +

release: dist clean
	python setup.py sdist upload
	python setup.py bdist_wheel upload

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean
	python setup.py install

erase_cassettes:
	rm -fr tests/cassettes/

scrub_cassettes:
	cd bin && ./scrub_cassettes.sh

run_tests:
	python setup.py test

test: run_tests scrub_cassettes

lint:
	flake8 narlivs/ tests/

coverage:
	coverage run setup.py test
	coverage report -m
