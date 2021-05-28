#!/bin/bash

# Processing original notebook to get rid of confusing markers in cells.

IN=flask.ipynb
OUT=flask_final.ipynb

echo "converting: $IN -> $OUT"

echo 'removing magic-cell markers: %% and !'
grep -v '%%' $IN | sed -e 's/"! /"/' > $OUT

echo "showing changes"
diff -U 1 $IN $OUT
