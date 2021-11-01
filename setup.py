from numpy.distutils.core import setup, Extension
from numpy.distutils.misc_util import Configuration
import distutils.sysconfig as ds
from setuptools import setup
import os, codecs, re

long_description = 'A Python package for generating light curves from TESS target pixel files.'

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

# DEPENDENCIES
# 1. What are the required dependencies?
with open('requirements.txt') as f:
    install_requires = f.read().splitlines()
# 2. What dependencies required to run the unit tests? (i.e. `pytest --remote-data`)
tests_require = ['pytest', 'pytest-cov', 'pytest-remotedata']


setup(name='sydsap',
      version=find_version("src", "__init__.py"),
      description='Generating TESS light curves.',
      long_description=long_description,
      author='Tim White',
      author_email='tim.white@sydney.edu.au',
      url='https://github.com/hvidy/sydsap',
      package_dir={'sydsap':'src'},
      # scripts=['bin/tessbkgd'],
      packages=['sydsap'],
      package_data={'': ['data/*.xml']},
      include_package_data=True,
      install_requires=install_requires,
      tests_require=tests_require,
      license='GPLv3',
      classifiers=[
          "Topic :: Scientific/Engineering",
          "Intended Audience :: Science/Research",
          "Intended Audience :: Developers",
          "Development Status :: 4 - Beta",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
          "Operating System :: OS Independent",
          "Programming Language :: Python"
      ]
     )
