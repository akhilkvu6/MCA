#!/bin/bash

if [ $# -eq 1 ]
then
    who > users.txt

    echo "$1 user is logged in:"

    grep -c "$1" users.txt
else
    echo "Please enter username"
fi