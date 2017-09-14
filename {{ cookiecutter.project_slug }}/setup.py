from setuptools import find_packages, setup


install_requires = [
    'django==1.11.5',
    'django-environ==0.4.4',
    'wagtail==1.12.1',
    'whitenoise==3.3.0',
]

docs_require = [
    'sphinx',
]

test_require = [
    'flake8',
    'isort',
    'pytest',
    'pytest-cov',
    'pytest-django',
    'tox',
]

setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.project_short_description }}',
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    install_requires=install_requires,
    extras_require={
        'docs': docs_require,
        'test': test_require
    },
    scripts=[
        'manage.py'
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: Unix',
        'Programming Language :: Python',
    ],
)
