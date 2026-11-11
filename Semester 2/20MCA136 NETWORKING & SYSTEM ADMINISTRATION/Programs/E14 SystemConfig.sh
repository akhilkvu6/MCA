#!/bin/bash

echo "===== SYSTEM CONFIGURATION ====="

echo "Current Shell: $SHELL"

echo "------------------------"

echo "Home Directory: $HOME"

echo "------------------------"

echo "Operating System Type: $OSTYPE"

echo "------------------------"

echo "Current Working Directory:"
pwd

echo "------------------------"

echo "Current User:"
whoami

echo "------------------------"

echo "Hostname:"
hostname

echo "------------------------"

echo "Kernel Version:"
uname -r

echo "------------------------"

echo "System Architecture:"
uname -m

echo "------------------------"

echo "Present Date and Time:"
date

echo "------------------------"

echo "Logged In Users:"
who

echo "------------------------"

echo "Disk Space Information:"
df -h

echo "------------------------"

echo "Memory Information:"
free -h