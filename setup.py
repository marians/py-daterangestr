# encoding: utf-8

from distutils.core import setup

try:
    import pypandoc
    description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    description = ''

setup(name='daterangestr',
      version='0.0.2',
      description='Utility to convert strings like "201301-201302" to start and end datetime tuples',
      long_description=description,
      author='Marian Steinbach',
      author_email='marian@sendung.de',
      url='https://github.com/marians/py-daterangestr',
      py_modules=['daterangestr'])
