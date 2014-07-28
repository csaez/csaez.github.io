#!/bin/bash

git checkout master
git add -A
echo "Please type a commit message:"
read MESSAGE
git commit -m "$MESSAGE"
git push origin