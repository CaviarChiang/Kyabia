
SETTINGS=testsite.settings

# target: all - Default target. Does nothing.
all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

# target: help - Display callable targets.
help:
	@egrep "^# target:" [Mm]akefile

# target: install - install pip requirements
install:
	pip install -r requirements.txt

# target: migrate - migrate django database
migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py migrate --run-syncdb

# target: run - run the django dev server at port 8000
run:
	python3 manage.py runserver 8000

# target: restart - restart gunicorn & nginx to reflect changes made in the backend
reload:
	sudo systemctl restart gunicorn
	sudo systemctl reload nginx
	sudo service nginx restart

# target: freeze - reads the versions of all installed packages in the local virtualenv and then produces the requirements.txt file
freeze:
	pip freeze > requirements.txt

# target: collect - calls the "collectstatic" django command
collect:
	python3 manage.py collectstatic --settings=$(SETTINGS) --noinput
