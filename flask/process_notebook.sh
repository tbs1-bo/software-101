#!/bin/bash

IN=flask.ipynb
OUT=flask_final.ipynb

grep -v '%%' $IN > $OUT
