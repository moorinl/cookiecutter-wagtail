from setuptools import find_packages, setup


install_requires = [
    'django>=1.8,<1.10'
]

docs_require = [
    'sphinx'
]

test_require = [
    'flake8',
    'pytest',
    'pytest-cov',
    'pytest-django',
    'tox'
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
    packages=find_packages(),
    include_package_data=True,
    classifier=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: Unix',
        'Programming Language :: Python',
    ],
)
