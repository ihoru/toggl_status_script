# Python script to check if timer in Toggl Track is active

The provided script is a Python program that interacts with the Toggl Track API to check if a timer (of a provided user's API Token) is currently running. It can be used with command-line arguments or with a token specified in a local settings file.

> There are two modes of operation:
> 1. It can be run once to check the current status of the timer.
> 2. It can be run continuously (with the -c argument) to keep checking if the timer is active.

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

## Hint (a lifehack)

This script is especially useful in conjunction with a tool [telegram-send](https://github.com/rahiel/telegram-send). After setting it up you can use it like this: `./main.sh  -c && telegram-send "Toggl Track timer has finished"`

I even created an alias in `~/.bash_aliases` to be able to run it fast:

```sh
alias timer='/LOCAL_PATH/main.sh -c && telegram-send "Toggl Track timer has finished"'
```
