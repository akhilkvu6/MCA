#!/bin/bash

echo -n "Enter a Number: "
read n

if (( n % 2 == 0 ))
then
    echo "$n is an Even Number"
else
    echo "$n is an Odd Number"
fi