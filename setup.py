"""See README.md for package documentation."""

from io import open
from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

URL = 'https://github.com/Yeicor/joystick'

setup(
    name='joystick',
    version='0.0.1',
    description='A on screen joystick for Kivy.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=URL,
    author='Kivy',
    author_email='kivy@kivy.org',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='Kivy kivy-garden',

    packages=['joystick'],
    install_requires=[],
    package_data={'joystick': ['*.kv']},
    data_files=[],
    entry_points={},
    project_urls={
        'Bug Reports': URL + '/issues',
        'Source': URL,
    },
)
