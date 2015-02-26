# -*- coding: utf-8 -*-

"""
This is a setup.py script for packaging Windows executable.

Usage:
    python setup.py build
"""


from setuptools import setup, find_packages

setup(
    name="ava-key",
    version="0.1.0",
    description="Key generator and validator.",
    include_package_data=True,
    zip_safe=True,
    packages=find_packages(),
    install_requires=[
        'Click',
        'libnacl',
        'base58',
        'pyscrypt'
    ],
    entry_points={
        'console-scripts': [
            'ava-key = ava-key:cli',
        ]
    }
)