from .base import *

DEBUG = True

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
