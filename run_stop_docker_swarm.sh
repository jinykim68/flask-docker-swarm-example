#!/bin/bash

set -a
source .env
set +a

docker swarm leave --force
