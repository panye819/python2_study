#!/usr/bin/env bash
#i=5
i="abc"
expr $i + 6 &>/dev/null
if [ $? -eq 0 ]; then
    echo "i is a integer."
else
    echo "i is not a integer"
fi