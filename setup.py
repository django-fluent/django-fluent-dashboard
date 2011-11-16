#!/usr/bin/env python
from setuptools import setup, find_packages
from os.path import dirname, join

setup(
    name='django-fluent-dashboard',
    version='0.2.0',
    license='Apache License, Version 2.0',

    install_requires=[
        'django-admin-tools>=0.4.1',  # 0.4.1 is the first release with Django 1.3 support.
    ],

    description='Django Fluent Dashboard - An improved django-admin-tools dashboard for Django projects',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),

    author='Diederik van der Boor',
    author_email='opensource@edoburu.nl',

    url='https://github.com/edoburu/django-fluent-dashboard',
    download_url='https://github.com/edoburu/django-fluent-dashboard/zipball/master',

    packages=find_packages(),
    include_package_data=True,

    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
