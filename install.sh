#!/bin/bash

set -e
set -x

if [ -z "$VIRTUAL_ENV" ]; then
    python3 -m venv venv
    . ./venv/bin/activate
    pip install -r requirements.txt
fi


