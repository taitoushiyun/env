import sys
import os.path
from setuptools import setup, find_packages
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'navigation'))

with open('requirements.txt') as f:
    install_requires = f.readlines()

CURRENT_PYTHON = sys.version_info[:2]
MIN_PYTHON = (3, 4)

if CURRENT_PYTHON < MIN_PYTHON:
    sys.stderr.write("""
        ============================
        Unsupported Python Version
        ============================

        Python {}.{} is unsupported. Please use a version newer than Python {}.{}.
    """.format(*CURRENT_PYTHON, *MIN_PYTHON))
    sys.exit(1)

with open('VERSION') as f:
    VERSION = f.read().strip()

setup(
    name='navigation',
    version=VERSION,
    description='simple env for 2D navigation',
    url='fake',
    author='cq',
    author_email='cq@cq',
    license='',
    packages=[package for package in find_packages() if package.startswith('navigation')],
    zip_safe=False,
    # install_requires=install_requires,
    # tests_require=['pytest', 'mock'],
    python_requires='>=3.4',
    classifiers=[
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
        ],
)