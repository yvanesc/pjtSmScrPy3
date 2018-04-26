#!/bin/bash
# declare 
git add --all
git status
echo "------------------------------"
echo "Comments to add for the commit"
read cmt
echo "$cmt"
git commit -am "$cmt"
git push -u origin master
