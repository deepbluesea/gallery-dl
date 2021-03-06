#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

import sys
import os.path



try:
    from setuptools import setup
    has_setuptools = True
except ImportError:
    from distutils.core import setup
    has_setuptools = False


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    with open(path, encoding="utf-8") as file:
        return file.read()


# get version without importing the package
exec(read("gallery_dl/version.py"))

DESCRIPTION = ("Command-line program to download image-galleries and "
               "-collections from several image hosting sites")
LONG_DESCRIPTION = read("README.rst")

if "py2exe" in sys.argv:
    try:
        import py2exe
    except ImportError:
        sys.exit("Error importing 'py2exe'")
    params = {
        "console": [{
            "script": "./gallery_dl/__main__.py",
            "dest_base": "gallery-dl",
            "version": __version__,
            "description": DESCRIPTION,
            "comments": LONG_DESCRIPTION,
            "product_name": "gallery-dl",
            "product_version": __version__,
        }],
        "options": {"py2exe": {
            "bundle_files": 0,
            "compressed": 1,
            "optimize": 1,
            "dist_dir": ".",
            "packages": ["gallery_dl"],
            "dll_excludes": ["w9xpopen.exe"],
        }},
        "zipfile": None,
    }
elif has_setuptools:
    params = {
        "entry_points": {
            "console_scripts": [
                "gallery-dl = gallery_dl:main"
            ]
        }
    }
else:
    params = {
        "scripts": ["bin/gallery-dl"]
    }

setup(
    name="gallery_dl",
    version=__version__,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url="https://github.com/mikf/gallery-dl",
    download_url="https://github.com/mikf/gallery-dl/releases/latest",
    author="Mike Fährmann",
    author_email="mike_faehrmann@web.de",
    maintainer="Mike Fährmann",
    maintainer_email="mike_faehrmann@web.de",
    license="GPLv2",
    python_requires=">=3.4",
    install_requires=[
        "requests >= 2.4.2",
    ],
    packages=[
        "gallery_dl",
        "gallery_dl.extractor",
        "gallery_dl.downloader",
        "gallery_dl.postprocessor",
    ],
    keywords="image gallery downloader crawler scraper",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Utilities",
    ],
    test_suite="test",
    **params
)
