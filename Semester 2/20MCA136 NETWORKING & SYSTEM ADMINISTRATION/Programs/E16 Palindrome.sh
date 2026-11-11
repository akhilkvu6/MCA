#!/bin/bash

echo -n "Enter a Number: "
read n

temp=$n
rev=0

while (( n > 0 ))
do
    rem=$(( n % 10 ))
    rev=$(( rev * 10 + rem ))
    n=$(( n / 10 ))
done

if (( temp == rev ))
then
    echo "$temp is a Palindrome Number"
else
    echo "$temp is Not a Palindrome Number"
fi