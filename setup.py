from setuptools import setup

with open("README.md", "r") as readme:
    description = readme.read()

with open("LICENSE", "r") as readme:
    license_x = readme.read()

with open("version.txt", "r") as readme:
    version_x = readme.read()

license_x_y = " : ".join(x for x in license_x.split("\n")[:3] if x)

description = "{} \n\n {}".format(description, license_x_y)

setup(
    name='jangli',
    version=version_x,
    packages=['jangli'],
    url='https://github.com/AbhimanyuHK/Json_Object_Conv',
    license=license_x_y,
    author='Abimanyu H K',
    author_email='manyu1994@hotmail.com',
    description='Data Object Mapping',
    long_description=description,
    long_description_content_type="text/markdown"
)
