#!/bin/bash
# Script para generar y optimizar las imágenes para su destino final en la web
#
# By jEsuSdA 8)


cd to-web/

rm *.png

cp ../color/*.png .

mogrify -resize 200x200 *.png 

for i in *.png
do

	mogrify -colors 64 -depth 6  -dither FloydSteinberg  -strip -define png:color-type=3  "$i"

done

# ;)
