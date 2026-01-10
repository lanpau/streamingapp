# StreamLive Makefile

.PHONY: help setup backend-dev backend-test ios-generate ios-build ios-open clean docker-build docker-up docker-down

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

setup: ## Install dependencies and setup environment
	@./scripts/setup.sh

backend-dev: ## Start backend development server
	@./scripts/dev-backend.sh

backend-test: ## Run backend tests
	@cd backend && uv run pytest

ios-generate: ## Generate iOS project with Tuist
	@cd ios && mise exec -- tuist generate

ios-build: ## Build iOS app
	@cd ios && mise exec -- tuist build StreamLive --platform iOS

ios-open: ## Open iOS Xcode workspace
	@cd ios && open StreamLive.xcworkspace

clean: ## Clean generated files
	@rm -rf backend/.venv backend/__pycache__ backend/src/app/__pycache__
	@rm -rf ios/*.xcworkspace ios/*.xcodeproj ios/Derived
	@echo "✨ Cleaned generated files"

docker-build: ## Build backend Docker image
	@docker compose build api

docker-up: ## Run backend in Docker
	@docker compose up -d api

docker-down: ## Stop Docker containers
	@docker compose down
