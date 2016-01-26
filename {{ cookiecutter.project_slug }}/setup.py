from setuptools import find_packages, setup


setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    install_requires=[
        'django>=1.9,<1.10'
    ],
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
