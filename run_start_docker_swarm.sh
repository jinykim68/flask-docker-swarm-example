#!/bin/bash

set -a
source .env
set +a

docker swarm init
docker stack deploy -c docker-compose-swarm.yml flask-docker-swarm-example
