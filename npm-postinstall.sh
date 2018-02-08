#!/bin/bash

# Copy bootstrap assets
cp -Rf node_modules/bootstrap-sass/assets/stylesheets/* _sass/
cp -Rf node_modules/bootstrap-sass/assets/fonts/* css/fonts/

# Copy font-awesome assets
cp -Rf node_modules/font-awesome-sass/assets/stylesheets/* _sass/
cp -Rf node_modules/font-awesome-sass/assets/fonts/* css/fonts/

# Copy font-awesome assets
mkdir -p js/select2
cp -Rf node_modules/select2/dist/css/select2.css _sass/_select2.scss
cp -Rf node_modules/select2/dist/js/* js/select2
