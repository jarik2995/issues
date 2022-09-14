build-images:
	@echo "Building docker images"
	@docker build -t issues-app .
	@docker build -t issues-inventory ./test/inventory/
	@docker build -t issues-ssh ./test/

create-test-env:
	@echo "Generating ssh keypair and provisioning ssh servers"
	@if [ -f "/tmp/id_rsa" ]; then echo "ssh keys already exist"; else ssh-keygen -b 2048 -t rsa -f /tmp/id_rsa -N ''; fi
	@export SSH_PUBLIC_KEY="$(cat /tmp/id_rsa.pub)"; docker-compose --project-name=issues -f test/docker-compose.yml up -d

create-postgres:
	@echo "Provisioning postgres server and configuring database"
	@docker-compose --project-name=issues up -d issues-postgres && sleep 10
	@docker run --network=issues_default --env-file=.env -it issues-app python -m issues.test.create_database

run:
	@echo "Starting application"
	@docker-compose --project-name=issues up -d issues-scheduler issues-redis issues-worker

query-db:
	@echo "Getting data from database"
	@docker run --network=issues_default --env-file=.env -it issues-app python -m issues.test.get_host_issues
