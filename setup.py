import sys
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


if sys.version_info < (3, 4):
    sys.exit('Sorry, Python < 3.4 is not supported')

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
      name='pyvigicrues',
      version='0.0.1',
      description='Get level and speed from many French rivers (https://www.vigicrues.gouv.fr/)',
      long_description=long_description,
      author='Mickael HUBERT',
      author_email='github@winlux.fr',
      url='https://github.com/Mickaelh51/pyVigicrues',
      package_data={'': ['LICENSE']},
      include_package_data=True,
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'pyvigicrues = pyvigicrues.__main__:main'
          ]
      },
      license='MIT',
      install_requires=['requests'],
      classifiers=[
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ]
)
