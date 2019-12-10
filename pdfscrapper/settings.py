CORE_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'corsheaders,',
    'django_filters',
    'django_extensions',
]

LOCAL_APPS = [
    'pdfscrapper.apps.documents',
]

INSTALLED_APPS = CORE_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pdfscrapper.urls'

WSGI_APPLICATION = 'pdfscrapper.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'scrapperdb',
        'USER': 'scrapper',
        'PASSWORD': None,
        'HOST': 'localhost',
        'PORT': 5432
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGGING_LEVEL = 'INFO'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'WARNING',
        'handlers': ['console', 'urllib3', ],
    },
    'formatters': {
        'standard': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': LOGGING_LEVEL,
            'filters': [],
            'formatter': 'verbose',
            'class': 'logging.StreamHandler',
        },
        'urllib3': {
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'urllib3': {
            'level': 'DEBUG',
            'handlers': ['urllib3', 'fluent'],
            'propagate': False,
        },
        'django': {
            'handlers': ['console', 'fluent'],
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console', 'fluent'],
            'level': LOGGING_LEVEL,
            'propagate': False,
        },
        'django.security': {
            'handlers': ['console', 'fluent'],
            'level': 'ERROR',
            'propagate': False,
        },
        'py.warnings': {
            'handlers': ['console', 'fluent'],
            'propagate': False,
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console', 'fluent'],
            'propagate': False,
        },
    },
}