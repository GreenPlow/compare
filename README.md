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
This will place the virtual enviroment in the `.venv` dir.
If the empty dir is not created the virtual env will default to another location.


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
This project is structured with `src` and `test` directories. To enable pytest to run in this structure, `setup.py` is used in combination with: 
```shell
pipenv install -e . --dev
```
to generate an editable install of the package.

### black
This project is formatted with black
```shell
pipenv run black --check .
```

remove `--check` to format
