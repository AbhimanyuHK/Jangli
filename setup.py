from setuptools import setup

with open("README.md", "r") as readme:
    description = readme.read()

with open("LICENSE", "r") as readme:
    license_x = readme.read()

setup(
    name='json_utils',
    version='1.0.0',
    packages=['json_utils'],
    url='https://github.com/AbhimanyuHK/Json_Object_Conv',
    license=license_x,
    author='Abimanyu H K',
    author_email='manyu1994@hotmail.com',
    description=description
)
