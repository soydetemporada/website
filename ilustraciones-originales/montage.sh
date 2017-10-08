#!/bin/bash 

# Script que crea un montaje con todas las imágenes de frutas y verduras del proyecto
#
# By jEsuSdA 8)

mkdir temp

cp color/*.color.png temp

mogrify -resize 100x100 temp/*.color.png 

montage temp/*.color.png -geometry 100x100+7+7   montaje.jpg

rm -rf temp

# ;)
