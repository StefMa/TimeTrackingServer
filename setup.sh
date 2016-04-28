#!/bin/bash

echo -n "Set project id: "
read project
sed -i '' "s/\[PROJECTID\]/$project/g" app.yaml

echo -n "Set basic auth username: "
read authUsername
sed -i '' "s/\[USERNAME\]/$authUsername/g" header_helper.py

echo -n "Set basic auth password: "
read authPassword
sed -i '' "s/\[PASSWORD\]/$authPassword/g" header_helper.py
