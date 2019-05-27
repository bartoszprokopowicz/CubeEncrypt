from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(

     name='CubeEncrypt',

     version='1.0',

     packages=find_packages(exclude=['tests*']),

     license="MIT",

     author="Bartosz Prokopowicz",

     author_email="bartosz.prokopowicz.97@gmail.com",

     description="Package to encrypt and decrypt strings",

     long_description=long_description,

     long_description_content_type="text/markdown",

     url="https://github.com/bartoszprokopowicz/CubeEncrypt",

     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],

 )