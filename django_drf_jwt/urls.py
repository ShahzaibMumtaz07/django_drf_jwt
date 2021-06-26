from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token


app_name = "django_drf_jwt"


urlpatterns = [
    path('api-token-auth/', obtain_jwt_token, name='obtain_jwt_token'),
]

