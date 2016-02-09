from setuptools import find_packages, setup


install_requires = [
    'django>=1.9,<1.10'
]

tests_require = [
    'flake8',
    'pytest',
    'tox'
]

setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.project_short_description }}',
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require
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
