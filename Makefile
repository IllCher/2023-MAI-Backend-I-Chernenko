up:
	docker-compose up -d

migrate:
	docker-compose run --rm django sh -c "python3 DjangoPrj/manage.py makemigrations; python3 DjangoPrj/manage.py migrate;"

test:
	docker-compose up -d && ./run.sh

usualtest:
	docker-compose run --rm django sh -c "python3 DjangoPrj/manage.py test app;"

checkcoverage:
	docker-compose run --rm django sh -c "coverage run --source='.' DjangoPrj/manage.py test app; coverage report;"
