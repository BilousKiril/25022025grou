PHONY: test
test:
	echo 'test started'
	pytest . -v






PHONY: check
check: test
	echo '1234'
	black .
	isort .
	flake8 .

