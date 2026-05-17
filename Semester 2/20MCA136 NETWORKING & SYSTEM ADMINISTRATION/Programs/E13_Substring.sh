#!/bin/bash

echo -n "Enter a String: "
read str

echo -n "Enter Starting Position: "
read pos

echo -n "Enter Length: "
read len

substr=${str:$pos:$len}

echo "Substring = $substr"