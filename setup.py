# -*- coding: utf-8 -*-
"""Setup module."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_requires():
    """Read requirements.txt."""
    requirements = open("requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))


def read_description():
    """Read README.md and CHANGELOG.md."""
    try:
        with open("README.md") as r:
            description = "\n"
            description += r.read()
        with open("CHANGELOG.md") as c:
            description += "\n"
            description += c.read()
        return description
    except Exception:
        return "Some useful script for Orangepi/Raspberrypi boards"


setup(
    name='orangetool',
    packages=['orangetool'],
    version='0.35',
    description='Some useful script for Orangepi/Raspberrypi boards',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    author='Moduland Co',
    author_email='info@moduland.ir',
    url='https://github.com/Moduland/Orangetool',
    download_url='https://github.com/Moduland/Orangetool/tarball/v0.35',
    keywords="orangepi raspberrypi embedded-systems python",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
    ],
    install_requires=get_requires(),
    license='MIT',
)
