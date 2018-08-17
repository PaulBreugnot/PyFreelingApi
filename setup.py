from setuptools import setup

setup(name='PyFreelingApi',
      version='0.1',
      url='https://github.com/PaulBreugnot/PyFreeling',
      author="Paul Breugnot",
      author_email='paul.breugnot@etu.emse.fr',
      packages=["pyFreelingApi", "pyFreelingApi.windows_api", "pyFreelingApi.linux_api"],
      description="Freeling Python APIs",
      long_description=open('README.md').read())
