#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import sys

f = open('README.rst')
long_description = f.read().strip()
long_description = long_description.split('split here', 1)[1]
f.close()

requires = [
    'nose',
]

setup(
    name='nose-audio',
    version='0.1.1',
    description="Add audio to your test suite",
    long_description=long_description,
    author='Ralph Bean',
    author_email='rbean@redhat.com',
    url='http://github.com/ralphbean/nose-audio/',
    license='LGPLv2+',
    classifiers=[
    ],
    install_requires=requires,
    packages=[
        'naudio',
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points = {
        'nose.plugins.0.10': [
            'naudio = naudio:NoseAudioPlugin',
        ]
    },
)
