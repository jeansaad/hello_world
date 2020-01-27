# -*- coding: utf-8 -*-

try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements
from pip.download import PipSession

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


links = []
requires = []

requirements_filename = 'requirements-to-freeze.txt'

try:
    # new versions of pip requires a session
    requirements = parse_requirements(requirements_filename,
                                      session=PipSession())
except TypeError:
    requirements = parse_requirements(requirements_filename)

for item in requirements:
    # we want to handle package names and also repo urls
    if getattr(item, 'url', None):  # older pip has url
        links.append(str(item.url))
    if getattr(item, 'link', None):  # newer pip has link
        links.append(str(item.link))
    if item.req:
        requires.append(str(item.req))

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='hello_world',
    version='0.1.0',
    description='A simple Hello World package',
    long_description=readme,
    author='Jean Saad',
    author_email='jeansaad@gmail.com',
    url='https://github.com/jeansaad/hello_world',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=requires,
    dependency_links=links,
    setup_requires=['green'],
)
