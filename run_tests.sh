#!/bin/sh

for d in matplotlib persistenz; do
    pytest --nbval $d || exit 1
done
