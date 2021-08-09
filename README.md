## Compare
This project is a work in progress. It is not complete.
### Use
To use, call the main.py from the terminal with the `source` and `destination` paths.

Command Line Arguments:

|Arguments|Description|
|:---|:---|
|origin|Path to the directory files will be copied from.|
|destination|Path to the directory files will be copied to.|
|--hidden|Optional! Script will evaluate hidden and copy hidden files.|

### To develop
1) Make a .venv dir in the project root
```shell
$ mkdir .venv
```

2) To initialize a Python 3 virtual environment, run:
```shell
$ pipenv --three
```
This will place the virtual environment in the `.venv` directory.
The virtual env will default to another location if an empty directory isn't created,


3) To install dependencies (need --dev for dev dependencies), run:
```shell
$ pipenv install
```

To activate this project's virtualenv, run:
```shell
$ pipenv shell
```

To remove the virtual env, run:
```shell
$ pipenv --rm
```

### pytest
Project structured with `src` and `test` directories. To enable pytest to run in this structure, `setup.py` is used in combination with: 
```shell
pipenv install -e . --dev
```
to generate an editable install of the package.

### black
Project formatted with black.
```shell
pipenv run black --check .
```

remove `--check` to format
