IMAGE_NAME=rpi4-dashboard
TAG=latest
REQUIREMENTS_FILE=requirements.txt

.PHONY: help
 
help:  ## Help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

freeze: ## Freezing dependencies
	@echo "Freezing..."
	pip freeze >> ${REQUIREMENTS_FILE}

install: ## Install dependencies
	@echo "Installing..."
	pip install -r ${REQUIREMENTS_FILE}

build: ## Build Docker App 
	@echo "Building..."
	docker build --no-cache -t  ${IMAGE_NAME}:${TAG} .

run: build ## Run DockerApp
	@echo "Running..."
	docker run -p 8000:8000  ${IMAGE_NAME}:${TAG}
