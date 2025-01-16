.PHONY: app
app:
		docker compose exec medical_text_classifier bash
up:
		docker compose up -d
down:
		docker compose down --remove-orphans
restart:
	@make down
	@make up
logs:
		docker compose logs -f
