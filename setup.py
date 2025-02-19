#!/usr/bin/env python3
from setuptools import setup


setup(
    name='filexture',
    version='0.1.0a1',
    description="A tool to create print and play card games",
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest'
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Typing :: Typed',
    ],
    keywords='',
    author='Pablo Muñoz',
    author_email='pablerass@gmail.com',
    url='https://github.com/pablerass/filexture',
    license='MIT',
    entry_points={
        'pytest11': [
            "filexture = filexture",
        ],
    },
    packages=['filexture'],
    install_requires=[line for line in open('requirements.txt')],
    python_requires='>=3.10'
)