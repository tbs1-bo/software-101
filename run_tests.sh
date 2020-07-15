#!/bin/sh

# TODO better use negative list of dirs not to check instead of positive list.

for d in matplotlib persistenz; do
    echo testing $d
    venv/bin/pytest --nbval $d || exit 1
done
