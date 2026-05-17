#!/bin/bash

echo "===== SIMPLE CALCULATOR ====="

echo -n "Enter First Number: "
read n1

echo -n "Enter Second Number: "
read n2

echo "Choose Operation"
echo "1. Addition"
echo "2. Subtraction"
echo "3. Multiplication"
echo "4. Division"

echo -n "Enter Choice: "
read ch

case $ch in
    1)
        result=$((n1 + n2))
        echo "Result = $result"
        ;;
    2)
        result=$((n1 - n2))
        echo "Result = $result"
        ;;
    3)
        result=$((n1 * n2))
        echo "Result = $result"
        ;;
    4)
        if [[ $n2 -eq 0 ]]
        then
            echo "Division by zero is not possible"
        else
            result=$((n1 / n2))
            echo "Result = $result"
        fi
        ;;
    *)
        echo "Invalid Choice"
        ;;
esac