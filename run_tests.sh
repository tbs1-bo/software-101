#!/bin/sh

for d in decorator matplotlib persistenz; do
    pytest --nbval $d || exit 1
done
