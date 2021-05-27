#!/bin/bash

IN=flask.ipynb
OUT=flask_final.ipynb

echo "converting: $IN -> $OUT"

echo 'removing magic-cell markers: %%'
grep -v '%%' $IN > $OUT

