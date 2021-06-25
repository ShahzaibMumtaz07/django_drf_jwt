from django.conf import settings
from datetime import datetime


settings.INSTALLED_APPS += [
    'rest_framework',
]


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
   'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'

}


JWT_AUTH = {
    # how long the original token is valid for
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=0.41666667),

    # allow refreshing of tokens
    'JWT_ALLOW_REFRESH': True,

    # this is the maximum time AFTER the token was issued that
    # it can be refreshed.  exprired tokens can't be refreshed.
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=0.41666667),
}

