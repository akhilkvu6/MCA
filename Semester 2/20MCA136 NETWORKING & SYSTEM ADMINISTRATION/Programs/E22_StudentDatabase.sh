#!/bin/bash

ch_cont="y"

read -p "Enter database name: " db

while [ "$ch_cont" = "y" ]
do
    echo "1. View Database"
    echo "2. View Specific Record"
    echo "3. Add Record"
    echo "4. Delete Record"
    echo "5. Exit"

    read -p "Enter choice: " ch

    case $ch in

    1)
        cat "$db"
        ;;

    2)
        read -p "Enter ID: " id
        grep "^$id " "$db"
        ;;

    3)
        read -p "Enter ID Name Course College: " rec
        echo "$rec" >> "$db"
        ;;

    4)
        read -p "Enter ID: " id
        grep -v "^$id " "$db" > temp
        mv temp "$db"
        echo "Record deleted"
        ;;

    5)
        exit
        ;;

    *)
        echo "Invalid choice"
        ;;

    esac

    read -p "Continue? (y/n): " ch_cont
done