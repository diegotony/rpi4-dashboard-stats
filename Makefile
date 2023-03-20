IMAGE_NAME=rpi4-dashboard
TAG=latest
REQUIREMENTS_FILE=requirements.txt
ENV_FOLDER=.env
SHELL := /bin/bash
PIP=${ENV_FOLDER}/bin/pip
.PHONY: help
 
help:  ## Help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

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
	docker run -p 8000:8000  ${IMAGE_NAME}:${TAG}
