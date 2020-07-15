#!/bin/sh

for d in matplotlib persistenz; do
    echo testing $d
    venv/bin/pytest --nbval $d || exit 1
done
