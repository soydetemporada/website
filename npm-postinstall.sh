#!/bin/bash

# Copy bootstrap assets
cp -Rf node_modules/bootstrap-sass/assets/stylesheets/* _sass/
cp -Rf node_modules/bootstrap-sass/assets/fonts/* css/fonts/

# Copy font-awesome assets
cp -Rf node_modules/font-awesome-sass/assets/stylesheets/* _sass/
cp -Rf node_modules/font-awesome-sass/assets/fonts/* css/fonts/
