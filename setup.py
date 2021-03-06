#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'marvinbot'
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='marvinbot_cinema_plugin',
    version='0.1.0',
    description="Plugin to know the availables movies in local theaters",
    long_description=readme,
    author="Jearel Alcántara",
    author_email='jeasoft@gmail.com',
    url='https://github.com/jeasoft/marvinbot_cinema_plugin',
    packages=[
        'marvinbot_cinema_plugin',
    ],
    package_dir={'marvinbot_cinema_plugin':
                 'marvinbot_cinema_plugin'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='marvinbot_cinema_plugin',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    dependency_links=[
        'git+ssh://git@github.com:BotDevGroup/marvin.git#egg=marvinbot',
    ],
)
