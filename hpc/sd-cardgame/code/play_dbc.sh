#!/bin/sh

python dbc/main.py
find . -name '*.pyc' -delete
