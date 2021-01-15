import setuptools
from os import system
from platform import system as opsystem

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
    python_requires = '>=3.6'
)

if opsystem() == 'Linux':
    system('chmod +x zget.py ; cp zget.py ./zget ; dos2unix zget ; mv zget /usr/bin/')
