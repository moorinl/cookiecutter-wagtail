from {{ cookiecutter.project_slug }}.settings.base import *  # noqa


try:
    from {{ cookiecutter.project_slug }}.settings.local import *  # noqa
except ImportError:
    pass
