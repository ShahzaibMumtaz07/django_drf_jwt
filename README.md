# Django REST Framework JWT Example

A simple app to use django-jwt-authentication using Django REST Framework
## Running the Project Locally

First, add this to your requirements file of the project:

```bash
pip install django-drf-jwt
```

Install the requirements:

```bash
pip install -r requirements.txt
```
Add app to the INSTALLED_APPS in the project:
```bash
INSTALLED_APPS = [
    ...,
    'django_drf_jwt',
    ...,
]
```
Include the app urls in your project urls.py:
```bash
from django.urls import path, include

urlpatterns = [
    path('django_drf_jwt/', include('django_drf_jwt.urls'))
]
```


Apply the migrations if not applied:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The API endpoints will be available at **127.0.0.1:8000/django_drf_jwt/api-token-auth/**

