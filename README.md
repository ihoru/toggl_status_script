# Python script to check if timer in Toggl Track is active

## Create environment

One of ways of creating an environment is to use [pipenv](https://github.com/pypa/pipenv):

```sh
cd $DIR # open a directory, where the source code was cloned
pipenv shell
```

If you use another way, then execution with `./main.sh` will not work.

## Install dependencies

```sh
pipenv sync
```

or

```sh
pip install -r requirements.txt
```

## Settings setup (optional)

If you don't want to specify API Token in script's arguments every execution create file `src/local_settings.py` like
this:

```sh
cd $DIR
cp src/example.local_settings.py src/local_settings.py
vim src/local_settings.py
```

## Execution

```sh
cd $DIR
./main.sh
```

or

```sh
$DIR/main.sh
```

## Arguments

- Pass argument `-c` to continuously check timer if it is active
- Pass `--token TOKEN` if needed to overwrite settings
- Use `-h` to see all available options (help)

## Alternative way of execution

```sh
python src/main.py
```
