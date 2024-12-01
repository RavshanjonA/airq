run-server:
	poetry run python3 manage.py runserver
migrate:
	poetry run python3 manage.py migrate
mig:
	poetry run python3  manage.py makemigrations
collect:
	poetry run python3 manage.py collectstatic
app:
	poetry run python3 manage.py startapp $(name)
install:
	poetry install
add:
	poetry add $(package)
# more than one packages: make add package="pillow psycopg2-binary"
superuser:
	poetry run python3 -m manage.py createsuperuser --username=$(username) --email=$(email)
req:
	poetry export --without-hashes --format=requirements.txt > requirements.txt
check:
	ruff check .