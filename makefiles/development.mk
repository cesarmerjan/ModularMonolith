.PHONY: shell
shell:
	${DOCKER_COMPOSE} run --rm -it shell

.PHONY: bash
bash:
	${DOCKER_COMPOSE} run --rm -it bash


.PHONY: notification
notification:
	${DOCKER_COMPOSE} run --rm --service-ports notification


.PHONY: database-ui
database-ui: database
	${DOCKER_COMPOSE} up database-ui -d


.PHONY: database-client
database-client:
	${DOCKER_COMPOSE} run --rm -it database-client