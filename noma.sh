#!/bin/bash

python /usr/share/noma/checkfolder.py
echo $1 > ~/.noma/thefilename.txt
python /usr/share/noma/program.py