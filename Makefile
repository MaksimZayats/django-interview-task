run.bot:
	python -m bot

run.server.local:
	sh ./run-local.sh

run.server.prod:
	python -m gunicorn api.web.wsgi:application \
		--bind 0.0.0.0:80 \
		--workers ${WORKERS} \
		--timeout 480

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

collectstatic:
	python manage.py collectstatic --no-input

createsuperuser:
	python manage.py createsuperuser --email "" --username admin

# Tests, linters & formatters
fmt:
	make -k ruff-fmt black

lint:
	make -k ruff black-check mypy

black:
	python -m black .

black-check:
	python -m black --check .

ruff:
	python -m ruff .

ruff-fmt:
	python -m ruff --fix-only --unsafe-fixes .

test:
	python -m pytest

mypy:
	python -m mypy .
