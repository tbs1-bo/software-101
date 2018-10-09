#!/bin/bash

FILE=${1:?"No file given"}
DIR=$(dirname $FILE)
FILEMD=$(basename $FILE .ipynb).md

# Convert Notebook to markdown
jupyter nbconvert --to markdown --output $FILEMD $FILE

# remove magic cell information
# -i work in-place with no backup files ("")
#
echo removing magic lines from $DIR/$FILEMD
sed -i '' -e "/%%writefile/d; /^    Writing /d; /^    Overwriting/d; /^    Appending/d; s/^! //" $DIR/$FILEMD
echo removing ansi escape sequences
# <ESC>  [  0  ;  1  ;  4  m
sed -i '' -e "s/\x1b\[[0-9]*;*[0-9]*;*[0-9]*m//g" $DIR/$FILEMD
