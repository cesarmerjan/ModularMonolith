.PHONY: application-image
application-image:
	docker build -t mega-services-dev:local \
	--no-cache \
	--target staging \
	-f ./docker/Dockerfile .
	docker tag mega-services-dev:local mega-services-dev:latest


.PHONY: database-client-image
database-client-image:
	docker build -t database-client-dev:local \
	--no-cache \
	-f ./docker/DatabaseClient .
	docker tag database-client-dev:local database-client-dev:latest


.PHONY: database
database:
	${DOCKER_COMPOSE} up database -d --force-recreate

.PHONY: database-destroy
database-destroy:
	${DOCKER_COMPOSE} down database --remove-orphans --volumes


.PHONY: infrastructure
infrastructure: database
