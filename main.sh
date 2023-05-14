#!/bin/bash

DIR=$(dirname "$0")
cd $DIR || exit 1
ENV_PATH=$(pipenv --venv -q 2>/dev/null)
if [[ "$ENV_PATH" == "" ]]; then
    echo "Environment was not found" >/dev/stderr
    exit 1;
fi;
source "$ENV_PATH/bin/activate"
python src/main.py $@
