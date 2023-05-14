#!/bin/bash

DIR=$(dirname "$0")
cd $DIR || exit
source "$(pipenv --venv -q)/bin/activate" && python src/main.py $@
