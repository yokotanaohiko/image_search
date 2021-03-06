import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "image_search",
    version = "0.0.1",
    author = "yokotanaohiko",
    author_email = "iam4570@yahoo.co.jp",
    description = read('README.md'),
    license = "BSD",
    keywords = "line bot",
    url = "",
    packages=['an_example_pypi_project', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
