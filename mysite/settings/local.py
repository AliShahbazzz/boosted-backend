from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'HOST': 'hiredin-db.postgres.database.azure.com',
        'USER': 'hiredin@hiredin-db',
        'PASSWORD': 'mbgdesk@123@098',
        'PORT': '5432'
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'lbqjychj',
#         'HOST': 'ruby.db.elephantsql.com',
#         'USER': 'lbqjychj',
#         'PASSWORD': 'zEDU_8yJ-sw22rt7O_RtZ_yL3Q9Fn_yb',
#         'PORT': '5432'
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# SSL ======================================================================================================================================================
CORS_REPLACE_HTTPS_REFERER = False
HOST_SCHEME = "http://"
SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = None
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_FRAME_DENY = False
