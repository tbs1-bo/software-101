#!/bin/sh

for d in matplotlib persistenz; do
    echo testing $d
    pytest --nbval $d || exit 1
done
