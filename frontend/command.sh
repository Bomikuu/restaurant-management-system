#!/bin/bash
npm install
rm -rf .cache
npm cache clean -f

yarn add @vue/cli-service
yarn 
yarn serve

