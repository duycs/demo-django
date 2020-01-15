# Demo Django
- Django 3
- RestAPI
- Authentication with JWT
- MySQL

### Installation
- Install Python 3.6.x
- Install Django 3
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
- Install libs at requirements file.
```
pip install -r requirements.txt
```
- Install Django rest swagger.
```
 pip install django-rest-swagger
```
6. Migrate.
```
python manage.py migrate
```
7. Run at local.
```
python manage.py runserver
```

### Create new app
1. Create folder where create app
```
mkdir /demo/apps/app-names
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

### TODO:
- Refresh-token
- Authorzation
- Modeling
- Aggregate relations

### References
- https://docs.djangoproject.com/en/3.0/
- https://www.django-rest-framework.org/tutorial/
- https://thinkster.io/tutorials/django-json-api/
- https://django-rest-swagger.readthedocs.io/en/latest/
- https://github.com/axios/axios