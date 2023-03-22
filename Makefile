IMAGE_NAME=rpi4-dashboard
TAG=latest
REQUIREMENTS_FILE=requirements.txt
ENV_FOLDER=.env
SHELL := /bin/bash
PIP=${ENV_FOLDER}/bin/pip
.PHONY: help
 
help:  ## Help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

requirements: ## Install requirements
	# Install tilt
	curl -fsSL https://raw.githubusercontent.com/tilt-dev/tilt/master/scripts/install.sh | bash

create_env: ## Create Environment
	pip install virtualenv
	virtualenv ${ENV_FOLDER}

freeze: ## Freezing dependencies
	@echo "Freezing..."
	${PIP} freeze >> ${REQUIREMENTS_FILE}

install: create_env ## Install dependencies
	@echo "Installing..."
	${PIP} install -r ${REQUIREMENTS_FILE}

build: ## Build Docker App 
	@echo "Building..."
	docker build --no-cache -t  ${IMAGE_NAME}:${TAG} .

run: build ## Run DockerApp
	@echo "Running..."
	@echo -e "docker_compose(\"./docker-compose.yml\")\ndocker_build(\"${IMAGE_NAME}\", context=\".\",dockerfile=\"Dockerfile\",live_update=[sync(\"app.py\", \"/app/app.py\"),sync(\"templates/\", \"/app/templates/\")])" > Tiltfile
	tilt up
	# docker run -p 8000:8000  ${IMAGE_NAME}:${TAG}
