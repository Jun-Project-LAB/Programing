#!/usr/bin/sh
msg=$(date)

git add .
git commit -m "${msg}"
git push origin main
