build:
	docker compose build --no-cache
	docker compose up -d
	docker exec -it fprocessor_service pytest -v

test: 
	docker exec -it fprocessor_service pytest -v

up:
	docker compose up

ps:
	docker compose ps

down:
	docker compose down

