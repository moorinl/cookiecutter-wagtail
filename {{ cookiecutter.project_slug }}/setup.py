from setuptools import find_packages, setup


install_requires = [
    'django>=1.10',
    'wagtail>=1.8'
]

docs_require = [
    'sphinx==1.4.5'
]

test_require = [
    'flake8==3.0.4',
    'isort==4.2.5',
    'pytest==2.9.2',
    'pytest-cov==2.3.1',
    'pytest-django==2.9.1',
    'tox==2.3.1'
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
    classifier=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: Unix',
        'Programming Language :: Python',
    ],
)
