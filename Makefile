build:
	docker compose build --no-cache

test: 
	pytest -s

up:
	docker compose up 

ps:
	docker compose ps

down:
	docker compose down

exec:
	docker exec -it ml_turnover_service bash

logs:
	docker compose logs -f

# DANGEROUS
reset:
	@
	make down
	docker rmi ml_turnover_service 
	docker compose build --no-cache 
	docker compose up

