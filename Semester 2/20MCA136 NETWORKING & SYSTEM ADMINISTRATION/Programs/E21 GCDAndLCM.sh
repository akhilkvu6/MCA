#!/bin/bash

echo -n "Enter First Number: "
read n1

echo -n "Enter Second Number: "
read n2

a=$n1
b=$n2

while (( b != 0 ))
do
    temp=$b
    b=$(( a % b ))
    a=$temp
done

gcd=$a
lcm=$(( (n1 * n2) / gcd ))

echo "GCD = $gcd"
echo "LCM = $lcm"