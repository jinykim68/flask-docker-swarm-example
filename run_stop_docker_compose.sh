#!/bin/bash

set -a
source .env
set +a

docker-compose --file ./docker-compose.yml down
