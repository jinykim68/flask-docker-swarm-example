# flask-docker-swarm-example

A simple **Flask** application running in **Docker** / **Docker Swarm** mode.

## Getting Started

### Prerequisites

*Docker Engine* needs to be installed on your machine ([Docker Documentation](https://docs.docker.com/)).

### Environment variables

| Variable                 | Description                                                               |
| ------------------------ | ------------------------------------------------------------------------- |
| `RABBITMQ_ERLANG_COOKIE` | Set a consistent cookie (useful for clustering) for **RabbitMQ**          |
| `RABBITMQ_DEFAULT_USER`  | Set a default username for **RabbitMQ**                                   |
| `RABBITMQ_DEFAULT_PASS`  | Set a default username's password for **RabbitMQ**                        |
| `RABBITMQ_NODE_PORT`     | Set a port number of RabbitMQ node (e.g., *5672*)                         |
| `CELERY_BROKER_URL`      | Set a location of the broker instance (i.e., **RabbitMQ URL**)            |
| `CELERY_RESULT_BACKEND`  | Set a location of result store (i.e., **Redis URL**)                      |
| `SESSION_TYPE`           | Set a type of server-side session store (i.e., **"redis"**)               |
| `SESSION_REDIS_URL`      | Set a location of server-side session store (i.e., **Redis URL**)         |

### Installing

To build application docker image,

```bash
./run_build_image.sh
```

**jinyoungk/flask-docker-swarm-example-app:latest** image will be generated.

```bash
$ docker images
REPOSITORY                                TAG     IMAGE ID      CREATED         SIZE
jinyoungk/flask-docker-swarm-example-app  latest  508adf7d3b65  26 minutes ago  288MB
```

To use this image in **Docker Swarm** mode, the image needs to be pushed.

```bash
$ docker login
Authenticating with existing credentials...
Login Succeeded

$ docker push jinyoungk/flask-docker-swarm-example-app:latest
The push refers to repository [docker.io/jinyoungk/flask-docker-swarm-example-app]
...
```

### Get it running

#### Run the application using docker-compose

```bash
$ ./run_start_docker_compose.sh
Creating network "flask-docker-swarm-example_example-network" with driver "bridge"
Creating flask-docker-swarm-example_reverse-proxy_1 ... done
Creating flask-docker-swarm-example_rabbitmq_1      ... done
Creating flask-docker-swarm-example_redis_1         ... done
Creating flask-docker-swarm-example_app-celery-worker_1 ... done
Creating flask-docker-swarm-example_app_1               ... done
Creating flask-docker-swarm-example_app_2               ... done
Creating flask-docker-swarm-example_app_3               ... done
```

To **stop** the application,

```bash
$ ./run_stop_docker_compose.sh
Stopping flask-docker-swarm-example_app_1               ... done
Stopping flask-docker-swarm-example_app_3               ... done
Stopping flask-docker-swarm-example_app_2               ... done
Stopping flask-docker-swarm-example_app-celery-worker_1 ... done
Stopping flask-docker-swarm-example_rabbitmq_1          ... done
Stopping flask-docker-swarm-example_redis_1             ... done
Stopping flask-docker-swarm-example_reverse-proxy_1     ... done
Removing flask-docker-swarm-example_app_1               ... done
Removing flask-docker-swarm-example_app_3               ... done
Removing flask-docker-swarm-example_app_2               ... done
Removing flask-docker-swarm-example_app-celery-worker_1 ... done
Removing flask-docker-swarm-example_rabbitmq_1          ... done
Removing flask-docker-swarm-example_redis_1             ... done
Removing flask-docker-swarm-example_reverse-proxy_1     ... done
Removing network flask-docker-swarm-example_example-network
```

#### Run the application in Docker Swarm mode

```bash
$ ./run_start_docker_swarm.sh
Swarm initialized: current node (2x8haqh70pu8ysej4gy0kryfm) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-1wmhdbgwzl0tlmsuurwnkjvsgk3nnnh5bz735epdr86cp1b6en-8un97xi65df647qiung9j3d23 192.168.65.3:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.

Creating network flask-docker-swarm-example_example-network
Creating service flask-docker-swarm-example_visualizer
Creating service flask-docker-swarm-example_app-celery-worker
Creating service flask-docker-swarm-example_app
Creating service flask-docker-swarm-example_reverse-proxy
Creating service flask-docker-swarm-example_rabbitmq
Creating service flask-docker-swarm-example_redis
```

To **list** services running,

```bash
$ docker service ls
ID                  NAME                                           MODE                REPLICAS            IMAGE                                             PORTS
qc8j43sx2jd7        flask-docker-swarm-example_app                 replicated          3/3                 jinyoungk/flask-docker-swarm-example-app:latest
oj04n3tqo361        flask-docker-swarm-example_app-celery-worker   replicated          1/1                 jinyoungk/flask-docker-swarm-example-app:latest
sz2npn8lxrl6        flask-docker-swarm-example_rabbitmq            replicated          1/1                 rabbitmq:3-alpine                                 *:15672->15672/tcp
tep634dw1893        flask-docker-swarm-example_redis               replicated          1/1                 redis:5-alpine
t4ee15srmdk6        flask-docker-swarm-example_reverse-proxy       replicated          1/1                 traefik:1.7-alpine                                *:80->80/tcp, *:8080->8080/tcp
0h5zv1puu7ib        flask-docker-swarm-example_visualizer          replicated          1/1                 dockersamples/visualizer:latest                   *:8888->8080/tcp
```

To **stop** the application,

```bash
$ ./run_stop_docker_swarm.sh
Node left the swarm.
```

## References

* [Traefik official docker image](https://hub.docker.com/_/traefik)
* [Docker Swarm Visualizer docker image](https://hub.docker.com/r/dockersamples/visualizer)
* [RabbitMQ official docker image](https://hub.docker.com/_/rabbitmq)
* [Redis official docker image](https://hub.docker.com/_/redis)
* [Github Traefik](https://github.com/containous/traefik)
* [Github Docker Swarm Visualizer](https://github.com/dockersamples/docker-swarm-visualizer)
* [Github Celery](https://github.com/celery/celery)
* [Github Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO)
* [Github Flask-Session](https://github.com/fengsp/flask-session)
