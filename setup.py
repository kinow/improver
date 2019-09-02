#!/usr/bin/env python

from setuptools import setup, find_packages

from glob import glob
from os.path import join

VERSION="0.0.1-dev"

INSTALL_REQUIRES = [
    'cf_units',
    'iris==2.1.*',
    'python-stratify',
    'numpy'
]
TESTS_REQUIRES = [
    'pytest==4.4.*'
]

EXTRAS_REQUIRE = {
    'doc': ['sphinx']
}
EXTRAS_REQUIRE['all'] = [y for x in EXTRAS_REQUIRE.values() for y in x]

setup(
    version=VERSION,
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    scripts=glob(join('bin', '*')),
    packages=find_packages("lib/"),
    package_dir={"": "lib"},
    package_data={
        'improver': [
            'bin/*'
        ]
    },
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    project_urls={
        "Documentation": "http://improver.readthedocs.io/en/latest/",
        "Source": "https://github.com/metoppv/improver",
        "Tracker": "https://github.com/metoppv/improver/issues"
    }
)
