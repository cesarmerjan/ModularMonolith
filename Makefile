PROJECT=modular_monolith
DOCKER_COMPOSE_FILE=docker/docker-compose.yaml
DOCKER_COMPOSE=docker compose -p ${PROJECT} -f ${DOCKER_COMPOSE_FILE} --env-file docker/docker.env

include makefiles/development.mk
include makefiles/infrastructure.mk
include makefiles/test.mk