TEST_TARGET = src/

## @ tests
.PHONY: _reports
_reports: ## Create the reports directory
	mkdir -p reports

.PHONY: unit-tests
unit-tests: _reports ## Run unit tests
	${DOCKER_COMPOSE} run --rm pytest ${TEST_TARGET} -m unit

.PHONY: integration-tests
integration-tests: _reports ## Run integration tests
	${DOCKER_COMPOSE} run --rm pytest ${TEST_TARGET} -m integration

.PHONY: end-to-end-tests
end-to-end-tests: _reports ## Run end-to-end tests
	${DOCKER_COMPOSE} run --rm pytest ${TEST_TARGET} -m end_to_end

.PHONY: system-architecture-tests
system-architecture-tests: _reports ## Run end-to-end tests
	${DOCKER_COMPOSE} run --rm pytest ${TEST_TARGET} -m system_architecture


# .PHONY: tests-coverage
# tests-coverage:
# 	${DOCKER_COMPOSE} run --rm coverage run -m pytest ${TEST_TARGET} -m "unit or integration or end_to_end"

.PHONY: tests
tests: system-architecture-tests unit-tests integration-tests end-to-end-tests
