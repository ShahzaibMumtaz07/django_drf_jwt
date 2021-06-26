from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='django_drf_jwt',
    version='0.0.6',
    description='A simple app to demonstrate django-jwt-authentication using Django REST Framework',
    url='https://github.com/ShahzaibMumtaz07/django_drf_jwt.git',
    author='Shahzaib Mumtaz',
    author_email='shahzaib.mumtaz.20195@gmail.com',
    package_dir = {'django_drf_jwt':'django_drf_jwt'},
    packages = ['django_drf_jwt'],
    install_requires=[
        'Django>=2.0.0',
        'djangorestframework>=3.12.4',
        'djangorestframework-jwt>=1.11.0',
        
      ],
    license = 'MIT',
    classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
        ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
