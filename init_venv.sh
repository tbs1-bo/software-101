#!/bin/bash

# install all dependencies for all topics
#
for f in */requirements.txt
do 
    echo $f 
    venv/bin/pip install -r $f
done
