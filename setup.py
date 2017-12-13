import os
from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
	README = readme.read()


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='django-bIo9',
	version='0.1',
	packages=find_packages(),
	license='BSD License',
	discription='a simple django app of blog site',
	long_discription=README,
	author='HuPeng',
	author_email='hpstrike@163.com',
	url='www.example.com',
	classifiers=[
		'Environment :: Web Environment',
		'Framework :: Django',
		'Programming Language :: Python :: 3.6',
		'Operating System :: OS Independent',
	],
)

