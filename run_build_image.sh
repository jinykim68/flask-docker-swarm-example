#!/bin/bash

image_name=jinyoungk/flask-docker-swarm-example-app
tag=latest

docker build --no-cache -t ${image_name}:${tag:-latest} -f ./docker/app/Dockerfile .
