build-images:
	@docker build -t issues-app .
	@docker build -t issues-inventory ./test/inventory/
	@docker build -t issues-ssh ./test/

create-test-env:
	@if [ -f "/tmp/id_rsa" ]; then echo "ssh keys already exist"; else ssh-keygen -b 2048 -t rsa -f /tmp/id_rsa -N '' <<< y; fi
	@docker-compose --env=PUBLIC_KEY="$(cat /tmp/id_rsa.pub)" --project-name=issues -f test/docker-compose.yml up -d

create-postgres:
	@docker-compose --project-name=issues up -d issues-postgres
	@docker run --network=issues_default --env-file=.env -it issues-app python -m issues.test.create_database

run:
	@docker-compose --project-name=issues up -d issues-scheduler issues-redis issues-worker

query-db:
	@docker run --network=issues_default --env-file=.env -it issues-app python -m issues.test.get_host_issues
