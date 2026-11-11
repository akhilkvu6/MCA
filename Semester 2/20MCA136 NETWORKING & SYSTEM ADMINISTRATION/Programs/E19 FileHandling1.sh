#!/bin/bash

echo "1. Create and Copy File"
echo "2. Print from Certain Line"
echo "3. Difference Between Two Files"
echo "4. Pattern Matching"

read -p "Enter Choice: " ch

case $ch in

1)
    read -p "Enter File Name: " f1

    echo "Enter Profile Details:"
    cat > "$f1"

    read -p "Enter Existing File Name to Copy Into: " f2

    cp "$f1" "$f2"

    echo "File copied successfully"
    ;;

2)
    read -p "Enter File Name: " file
    read -p "Enter Starting Line Number: " line

    tail -n +"$line" "$file"
    ;;

3)
    read -p "Enter First File Name: " f1
    read -p "Enter Second File Name: " f2

    diff "$f1" "$f2"
    ;;

4)
    read -p "Enter File Name: " file
    read -p "Enter Pattern: " pattern

    grep -n "$pattern" "$file"
    ;;

*)
    echo "Invalid Choice"
    ;;

esac