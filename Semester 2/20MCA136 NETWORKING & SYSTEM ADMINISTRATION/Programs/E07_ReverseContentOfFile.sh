#!/bin/bash

if [ $# -eq 1 ]
then
    if [ -f "$1" ]
    then
        echo "Contents of $1"
        cat "$1"

        echo "Reverse of $1"
        tac "$1"
    else
        echo "File does not exist!!"
    fi
else
    echo "Usage: $0 <filename>"
fi