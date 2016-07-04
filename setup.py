# -*- coding: utf-8 -*-
import io
import re
from setuptools import setup, find_packages
from distutils.core import Command
from unittest import TextTestRunner, TestLoader

with io.open('./pynes/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_match:
        VERSION = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

class TestCommand(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        loader = TestLoader()
        suite = loader.discover('pynes/tests', pattern='*_test.py')
        TextTestRunner(verbosity=4).run(suite)


setup(
    name='pyNES',
    version=VERSION,
    description='Python Programming for Nintendo 8bits',
    author="Gustavo Maia Neto (Guto Maia)",
    author_email="guto@guto.net",
    license="GPL3",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "examples"]),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Programming Language :: Assembly',
        'Topic :: Games/Entertainment',
        'Topic :: Software Development :: Assemblers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Compilers',
        'Topic :: Software Development :: Embedded Systems',
    ],
    url='http://github.com/gutomaia/pyNES/',
    cmdclass={'test': TestCommand},
    test_suite="pynes.tests",
)
