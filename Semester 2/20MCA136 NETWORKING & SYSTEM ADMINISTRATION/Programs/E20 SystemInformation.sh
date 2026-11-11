#!/bin/bash

echo "1. Count of users logged in:"
who | wc -l

echo "--------------------------------"

echo "2. Column list of files in home directory:"
ls -l $HOME | cut -c 17-24,39-50,56-

echo "--------------------------------"

echo "3. List of below priority jobs:"
ps -al | cut -c 16-19,70-

echo "--------------------------------"

echo "4. Current Date and Time:"
date

echo "--------------------------------"

echo "5. Current Working Directory:"
pwd

echo "--------------------------------"

echo "6. System Uptime:"
uptime

echo "--------------------------------"

echo "7. Disk Space Information:"
df -h