"""
Setup.py for tragger-travis
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='trigger-travis',
    version='0.0.3',
    description='',
    long_description='A CLI to trigger Travis CI builds and inject env vars',
    url='https://github.com/danielwhatmuff/trigger-travis',
    author='Daniel Whatmuff',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='travis builds ci deployments trigger',
    py_modules=["trigger-travis"],
    install_requires=['requests'],
    scripts=['bin/trigger-travis'],
)
