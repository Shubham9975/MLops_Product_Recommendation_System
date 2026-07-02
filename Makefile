build:
	docker build -t olist-recommender:latest .

run:
	docker run -p 8000:8000 olist-recommender:latest

compose:
	docker compose up --build

compose-detach:
	docker compose up -d --build

stop:
	docker compose down

test:
	pytest -v