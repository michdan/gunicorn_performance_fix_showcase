DOCKER_COMPOSE_COMMAND = docker-compose
DOCKER_COMPOSE_RUN ?= ${DOCKER_COMPOSE_COMMAND}  run --rm  -d
DOCKER_COMPOSE_UP ?= ${DOCKER_COMPOSE_COMMAND}  up  -d
PYTHON_RUN = python

# Sets everything up ready for `make start` to be run
init:
	@echo "  $(P) init"
	@make build

# Build
build:
	@echo "  $(P) build"
	${DOCKER_COMPOSE_COMMAND} build

start:
	${DOCKER_COMPOSE_UP}
