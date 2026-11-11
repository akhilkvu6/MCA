#!/bin/bash

echo -n "Enter a Word: "
read word

if grep -wq "$word" /usr/share/dict/words
then
    echo "$word exists in dictionary"
else
    echo "$word does not exist in dictionary"
fi