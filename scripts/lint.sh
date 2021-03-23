#!/bin/bash

# Copyright Contributors to the Open Cluster Management project

find crds -type f -name '*.yaml' -exec sh -c '
  for f do
    grep -Fxq "kind: CustomResourceDefinition" $f
    if [[ $? -ne 0 ]] ; then
        echo "Error in file $f, missing: kind: CustomResourceDefinition"
        exit 1
    fi
  done' sh {} +
