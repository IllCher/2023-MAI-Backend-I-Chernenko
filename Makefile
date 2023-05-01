up:
	docker-compose up -d

migrate:
	docker-compose run --rm django sh -c "python3 DjangoPrj/manage.py migrate"

test:
	docker-compose up -d && ./run.sh