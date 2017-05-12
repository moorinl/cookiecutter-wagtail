import os

import environ

env = environ.Env()


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

CACHES = {
    'default': env.cache(default='dummycache://'),
}

DATABASES = {
    'default': env.db_url(default='postgres://localhost/application'),
}

DEBUG = env.bool('DEBUG', default=False)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'wagtail.api.v2',
    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',

    'wagtail.contrib.modeladmin',
    'wagtail.contrib.settings',
    'wagtail.contrib.wagtailsitemaps',

    'modelcluster',
    'rest_framework',
    'taggit',

    'wagtailthemes',
]

INTERNAL_IPS = env.list('INTERNAL_IPS', default=['127.0.0.1'])

LANGUAGE_CODE = env.str('LANGUAGE_CODE', default='en-us')

MEDIA_URL = env.str('MEDIA_URL', default='/media/')
MEDIA_ROOT = env.str('MEDIA_ROOT', default=os.path.join(BASE_DIR, 'media'))

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = env.str('ROOT_URLCONF', default='{{ cookiecutter.project_slug }}.urls')

SECRET_KEY = env.str('SECRET_KEY', default='')

STATIC_URL = env.str('STATIC_URL', default='/static/')
STATIC_ROOT = env.str('STATIC_ROOT', default=os.path.join(BASE_DIR, 'static'))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'wagtailthemes.loaders.ThemeLoader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]

TIME_ZONE = env.str('TIME_ZONE', default='UTC')

USE_I18N = env.bool('USE_I18N', default=True)
USE_L10N = env.bool('USE_L10N', default=True)
USE_TZ = env.bool('USE_TZ', default=True)

WAGTAIL_SITE_NAME = env.str('WAGTAIL_SITE_NAME', default='{{ cookiecutter.project_name }}')

WSGI_APPLICATION = env.str('WSGI_APPLICATION', default='{{ cookiecutter.project_slug }}.wsgi.application')
