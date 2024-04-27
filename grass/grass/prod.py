import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
env = environ.Env(
    DEBUG=(bool, True)
)
CSRF_TRUSTED_ORIGINS = ["https://grass-job.ru",
                        "https://www.grass-job.ru",
                        ]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.get_value('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.get_value('DEBUG')
ALLOWED_HOSTS = env.get_value('ALLOWED_HOSTS').split()
REDIS_HOST = env.get_value('REDIS_HOST')
REDIS_PORT = env.get_value('REDIS_PORT')

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [(REDIS_HOST, REDIS_PORT)],
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}
