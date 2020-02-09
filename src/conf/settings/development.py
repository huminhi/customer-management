from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'NAME': 'cm_development',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'PORT': '5432',
    }
}
