#!/bin/bash

pyuic6 -x ./Qt_src/main.ui -o qt_main.py

for file in ./Qt_src/translations/*.ts; do
    pylupdate6 ./Qt_src/main.ui -ts "$file"
done

# Input your lrelease location
l_location="C:/Program Files (x86)/Qt Designer/lrelease.exe"

for file in ./Qt_src/translations/*.ts; do
    "$l_location" "$file" -qm ./Locales/$(basename "$file" .ts).qm
done