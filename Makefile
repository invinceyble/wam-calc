ENV='env_wam_calc'

default:
	@echo "Local running"
	@echo "make setup       Will setup your local environment"
	@echo "make run         Will run locally"
	@echo "make clean       Clean up the environment"


setup:
	test -d $(ENV) || virtualenv $(ENV)
	$(ENV)/bin/pip install -Ur requirements.txt

run:
	$(ENV)/bin/python app/app.py

clean:
	rm -rf $(ENV)
	find . -name *.pyc -type f -delete
	find . -name *.orig -type f -delete
	find . -name *.sw* -type f -delete
