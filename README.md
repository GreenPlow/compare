### compare


### to develop
1) Make a .venv dir in the project root
```shell
$ mkdir .venv
```

2) To initialize a Python 3 virtual environment, run:
```shell
$ pipenv --three
```
This will place the virtual enviroment in the `.venv` dir.
If the empty dir is not created the virtual env will default to another location.

To activate this project's virtualenv, run the following:
```shell
$ pipenv shell
```
This project is structured with separate src and test directories. To enable pytest to run in this structure, `setup.py` is used in combination with 
```
pipenv install -e . --dev
```
to generate an editable install of the package
