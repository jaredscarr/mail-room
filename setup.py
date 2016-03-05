# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='mail-room',
    description="An application for visualizing reports and donations",
    verion=0.1,
    author="Alex German and Jared Scarr",
    author_email="alexgerman11233@gmail.com jaredscarr@gmail.com",
    license='MIT',
    py_modules=['mail-room.py'],
    package_dir={'': 'mail-room'},
    install_requires=[],
    extras_requires={'test': ['pytest', 'pytest-xdist', 'tox']},
)
