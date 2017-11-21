#!/bin/bash

git pull origin develop

LC_ALL=en_US.UTF-8 bundle exec jekyll build --config _config-devel.yml
