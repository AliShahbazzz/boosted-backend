from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '12345abhiraj',
        'HOST': 'database-beta.cbjmo0koiyrt.us-east-2.rds.amazonaws.com',
        'PORT': '5432',
        # 'OPTIONS': {
        #         'sslmode':'verify-full',
        #         'sslrootcert': os.path.join(BASE_DIR, 'psql-ssl/server-ca.pem'),
        #         'sslcert': os.path.join(BASE_DIR, 'psql-ssl/client-cert.pem'),
        #         'sslkey': os.path.join(BASE_DIR, 'psql-ssl/client-key.pem'),
        #     }
    }
}
#db setting for heroku
# import dj_database_url
# db_from_env = dj_database_url.config()
# DATABASES['default'].update(db_from_env)
# DATABASES['default']['CONN_MAX_AGE'] = 500

#django mail admins sends error reports over mail to admin
ADMINS = (
    ('Your Name', 'Youremail@gmail.com'),
)

# SMTP ===================================================================================================================

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'youremial@gmail.com'
EMAIL_HOST_PASSWORD = '*********'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# SSL =====================================================================================================================
CORS_REPLACE_HTTPS_REFERER      = True
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY               = True