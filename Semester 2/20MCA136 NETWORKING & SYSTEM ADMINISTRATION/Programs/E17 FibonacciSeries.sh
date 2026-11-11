#!/bin/bash

echo -n "Enter Limit: "
read n

a=0
b=1

echo "Fibonacci Series:"

for (( i=0; i<n; i++ ))
do
    echo -n "$a "

    fn=$(( a + b ))
    a=$b
    b=$fn
done

echo