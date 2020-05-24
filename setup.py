from setuptools import find_packages, setup

with open('READ.md', 'r') as f:
	long_description = f.read()

setup(
	name='pgbackup',
	version='0.1.0',
	author='Michael Phan'
	authur_email='test@testmail.com'
	description='A utility for backuping up PostgreSQL databases.',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/eokim/testpgb',
	packages=find_packages('src')
)
