import setuptools
from os import system

setuptools.setup(
    name = 'zget-z3ox1s',
    version='0.0.1',
    author='z3ox1s',
    description = 'A tool to made HTTP Requests.',
    url = 'https://github.com/z3ox1s/zget',
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires = '>=3.0'
)

system('chmod +x zget.py ; mv zget.py zget ; mv zget /usr/bin/')
