#!/bin/bash
rm -rf node_modules
rm -rf .cache
npm cache clean -f
yarn add @vue/cli-service

yarn
yarn serve

