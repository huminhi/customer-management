from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'NAME': 'cm_production',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'PORT': '5432',
    }
}
