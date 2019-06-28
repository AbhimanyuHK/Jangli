@echo off

python setup.py sdist bdist_wheel

IF %ERRORLEVEL% NEQ 0 Exit /B 5

twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
