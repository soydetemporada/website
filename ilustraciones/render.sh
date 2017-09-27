#!/bin/bash

# Render icons from SVG to PNG
#
# by jEsuSdA 8)

for i in *.svg
do

inkscape -z -e "$i".png -w 1800 -h 1800 "$i"

done
