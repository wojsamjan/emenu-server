from emenu.settings import *


DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'emenudb',
        'USER': 'emenu',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
