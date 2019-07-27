# Playing with circleci and feature branches

[![CircleCI](https://circleci.com/gh/BernardNotarianni/spike-circleci.svg?style=svg)](https://circleci.com/gh/BernardNotarianni/spike-circleci)


### A workflow for feature branches

First create a github issue.

Then create a branch from origin/master:

    git checkout -b 3/change-message origin/master
    
Push it to github

    git push origin 3/change-message

Merge from master

    git merge origin/master
