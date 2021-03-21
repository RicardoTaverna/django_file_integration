# django_file_integration


## passo a passo
- pip install -r requirements.txt
- cd src
- docker-compose up -d
- python manage.py makemigrations
- python manage.py migrate
- python manage.py loaddata firstdata.json
- python manage.py runserver

## testes
- coverage run --source='.' manage.py test integration