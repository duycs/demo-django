# Demo Django

### Criteria
This project demo a backend RESTful API use Django framework

### Keywords
- Python
- Django
- RESTAPI
- Authentication with JWT
- MySQL

### Installation
- Install Python 3.6.x
- Install Django 2
```
python -m pip install Django
```
- Install Mysql
- Create/update *DATABASES* variables at *apps/settings.py* file to correct your local Mysql

### Stpes
1. Clone this repository.
2. Open terminal.
3. Go to root folder `demo-django`.
4. Install some libs.
```
pip install -r requirements.txt
```
5. Migrate.
```
python manage.py migrate
```
6. Run at local.
```
python manage.py runserver
```

### Create new app
1. Create folder where create app
```
mkdir ./demo/apps/app-names
```
2. Generate app-names
```
django-admin.py startapp app-name ./demo/apps/app-names
```
3. Add config app to settings
```
INSTALLED_APPS = [
....
    'demo.apps.app-names',
]
```

### TODO
- Refresh-token
- Logout will add token to black list
- Modeling with domain
- Aggregate relations
- Serializers
- Enpoints API for bussiness
- Containerization
- Authorization

### Bugs
- Swagger doc don't show if require authentication
- Swagger exception at Django 3
- Expired token time

### References
- https://docs.djangoproject.com/en/3.0/
- https://www.django-rest-framework.org/tutorial/
- https://thinkster.io/tutorials/django-json-api/
- https://github.com/gothinkster/conduit-django
- https://django-rest-swagger.readthedocs.io/en/latest/
- https://github.com/axios/axios
