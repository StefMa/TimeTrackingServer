#!/bin/bash

echo -n "Set project id: "
read project

sed -i '' "s/\[PROJECTID\]/$project/g" app.yaml
