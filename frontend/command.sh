#!/bin/bash
rm -rf node_modules package-lock.json && npm install
rm -rf .cache
npm cache clean -f

yarn add @vue/cli-service
yarn 
yarn serve

