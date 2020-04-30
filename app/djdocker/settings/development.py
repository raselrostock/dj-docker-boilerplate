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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}