#!/bin/bash

read -p "Enter directory name you want to search: " dir

direct="E:/MCA/S2/lab/$dir"

if [ -d "$direct" ]
then
    count=$(ls "$direct" | wc -l)
    echo "Number of files in $direct = $count"
else
    echo "Directory not found"
fi