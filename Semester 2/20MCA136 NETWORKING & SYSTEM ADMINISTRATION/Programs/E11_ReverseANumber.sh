#!/bin/bash

echo -n "Enter a Number: "
read n

rev=0

while (( n > 0 ))
do
    rem=$(( n % 10 ))
    rev=$(( rev * 10 + rem ))
    n=$(( n / 10 ))
done

echo "Reversed Number = $rev"