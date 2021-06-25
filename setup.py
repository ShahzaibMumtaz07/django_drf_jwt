from setuptools import setup

setup(
    name='django-rest-jwt',
    version='0.0.1',
    description='A simple app to demonstrate django-jwt-authentication using Django REST Framework',
    url='git@github.com:ShahzaibMumtaz07/django-rest-jwt.git',
    author='Shahzaib Mumtaz',
    author_email='shahzaib.mumtaz.20195@gmail.com',
    zip_safe=False,
    install_requires=[
        'Django',
        'djangorestframework',
        'djangorestframework-jwt',
        
      ],
)
