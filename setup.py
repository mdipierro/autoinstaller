#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='autoinstaller',
      version='0.1',
      description='A library that automatically imports from Pypi everything you try import',
      author='Massimo DiPierro',
      author_email='massimo.dipierro@gmail.com',
      long_description=open("README.md").read(),
      url='https://github.com/mdipierro/autoinstaller',
      install_requires=[],
      py_modules=["autoinstaller"],
      license= 'BSD',
      keywords='package management',
      )
