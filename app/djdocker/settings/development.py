from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = int(os.environ.get('DEBUG', default=0))
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

# SECRET_KEY = config('SECRET_KEY')
# DEBUG = config('DEBUG')
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']
# DJANGO_COLORS = config('DJANGO_COLORS')
################################
##    DATABASE CONFIGURATION  ##
################################

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}