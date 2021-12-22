# Django REST Framework JWT Example

A simple app to use django-jwt-authentication using Django REST Framework
## Running the Project Locally

In your requirements.txt:

```bash
django-drf-jwt
```

Install the requirements:

```bash
pip install -r requirements.txt
```

In your settings.py:

```bash
INSTALLED_APPS = [
    ...,
    'django_drf_jwt',
    ...,
]
```

In urls.py of project:

```bash
from django.urls import path, include

urlpatterns = [
    path('django_drf_jwt/', include('django_drf_jwt.urls'))
]
```


Make and Apply migrations:

```bash
python mananage.py makemigrations
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver 0.0.0.0:8000
```

Endpoint:**127.0.0.1:8000/django_drf_jwt/api-token-auth/**

