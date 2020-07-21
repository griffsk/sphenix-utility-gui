#!/usr/bin/env python3
from distutils.core import setup

setup(name='sPHENIX Utility GUI',
	version='1.0',
	description='Convert ADC zero suppression value to GeV',
	author='Spencer Griffith',
	author_email='spencer.griffith@colorado.edu',
	py_modules=['xmlFuncs'],
	scripts=['sphenix-utility.py'],
	)

