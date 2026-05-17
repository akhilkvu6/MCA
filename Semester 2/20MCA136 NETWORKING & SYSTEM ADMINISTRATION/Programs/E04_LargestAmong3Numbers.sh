#!/bin/bash

echo -n "Enter Number 1: "
read n1

echo -n "Enter Number 2: "
read n2

echo -n "Enter Number 3: "
read n3

if [[ $n1 -ge $n2 && $n1 -ge $n3 ]]
then
    echo "$n1 is the largest number"
elif [[ $n2 -ge $n1 && $n2 -ge $n3 ]]
then
    echo "$n2 is the largest number"
else
    echo "$n3 is the largest number"
fi