#!/bin/bash

set -a
source .env
set +a

docker-compose --file ./docker-compose.yml up --scale app=3 -d
