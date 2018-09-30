#!/bin/bash

FILE=${1:?"No file given"}
DIR=$(dirname $FILE)
FILEMD=$(basename $FILE .ipynb).md

# Convert Notebook to markdown
jupyter nbconvert --to markdown --output $FILEMD $FILE

# remove magic cell information
# -i work in-place with no backup files ("")
#
sed -i '' -e "/%%writefile/d; /^    Writing /d; /^    Overwriting/d; s/^! //" $DIR/$FILEMD
