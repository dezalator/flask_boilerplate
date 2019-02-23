include .env
up:
	docker-compose up -d
upb:
	docker-compose up -d --force-recreate --build
stop:
	docker-compose stop
db:
	export PGPASSWORD=${POSTGRES_PASSWORD}; docker exec -it db psql -U $(POSTGRES_USER) ${POSTGRES_DB}
r:
	docker exec -it redis  /usr/local/bin/redis-cli
test:
	docker exec -it api pytest
b:
	docker exec -it $(c) /bin/bash