#!/usr/bin/env python

# from distutils.core import setup, Extension
from setuptools import setup, Extension
import os
import codecs
import re

# Copied from wheel package
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(os.path.dirname(__file__), 'stillingerweber.py'),
                 encoding='utf8') as version_file:
    metadata = dict(re.findall(
        r"""__([a-z]+)__ = "([^"]+)""", version_file.read()))


long_desc = "".join(open("README.md").readlines())


setup(
    install_requires=[
        'autopep8==1.6.0',
        'numpy==1.22.2',
        "pycodestyle==2.8.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "toml==0.10.2; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'"],
    name='stillingerweber',
    version=metadata['version'],
    description='Stillinger-Weber potential function.',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
    py_modules=['stillingerweber'],
    author='Masakazu Matsumoto',
    author_email='vitroid@gmail.com',
    url='https://github.com/vitroid/StillingerWeber',
    keywords=[
        'stillinger-weber',
        'silicon',
        'potential'],
    license='MIT',
)
