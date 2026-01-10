BACKEND_CONTAINER_NAME = short-urls-backend
BACKEND_SERVICE_NAME = backend

compile:
	uv pip compile pyproject.toml -o requirements.txt

build:
	docker compose -f docker-compose.yaml build
up:
	docker compose -f docker-compose.yaml up -d
down:
	docker compose -f docker-compose.yaml down
restart:
	docker compose -f docker-compose.yaml down && docker compose -f docker-compose.yaml up -d
exec:
	docker exec -it $(BACKEND_CONTAINER_NAME) bash
logs:
	docker logs --tail 100 -f $(BACKEND_CONTAINER_NAME)

migrate:
	docker exec -t $(BACKEND_CONTAINER_NAME) alembic upgrade head

pre-commit:
	docker compose -f docker-compose.yaml run --rm $(BACKEND_SERVICE_NAME) bash -c 'git config --global safe.directory /code && PRE_COMMIT_HOME=.precomcache pre-commit run --all-files'
