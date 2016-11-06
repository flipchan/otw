import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "off the wire",
    version = "1.3",
    author = "Filip Kalebo",
    author_email = "flipchan@riseup.net",
    description = ("Off the wire crypto"),
    license = "Beerware",
    keywords = "encryption layerprox aes aes-ctr pgp hmac secure",
    url = "https://github.com/flipchan/otw",
    packages=['otw'],
    install_requires=['gnupg'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 5 - Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
