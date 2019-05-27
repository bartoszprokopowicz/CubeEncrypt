import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(

     name='CubeEncrypt',

     version='1.0',

     scripts=['Cube.py'],

     author="Bartosz Prokopowicz",

     author_email="bartosz.prokopowicz.97@gmail.com",

     description="Package to encrypt and decrypt string",

     long_description=long_description,

     long_description_content_type="text/markdown",

     url="https://github.com/bartoszprokopowicz/CubeEncrypt",

     packages=setuptools.find_packages(),

     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],

 )