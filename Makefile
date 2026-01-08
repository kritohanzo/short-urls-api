compile:
	uv pip compile pyproject.toml -o requirements.txt
build:
	docker compose -f docker-compose.yaml build
up:
	docker compose -f docker-compose.yaml up -d
down:
	docker compose -f docker-compose.yaml down
logs:
	docker logs --tail 100 -f short-urls-backend
migrate:
	docker exec short-urls-backend alembic upgrade head
exec:
	docker exec -it short-urls-backend sh
restart:
	docker compose -f docker-compose.yaml down && docker compose -f docker-compose.yaml up -d
pre-commit:
	pre-commit run --all-files
