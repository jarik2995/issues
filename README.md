### Problem statement:

```
Suppose we have a large set of machines running in a DC somewhere. A yaml list of these machines can be obtained from a URL which you should take as a configuration variable, and looks like this:
machine-1:
	ip: aa.bb.cc.dd
machine-2:
	ip: ee.ff.gg.hh
We would like the contents of the “/etc/issue” file on each of these machines to be readregularly (eg. every hour) and put into a PostgreSQL database.
```

# ISSUES
Issues app designed to collect content of /etc/issue from large amount of servers and safe it to database. It is build based on python beat celery framework which allows to run it in any containerized environemnt(docker-compose, kubernetes, etc..). As well celery allows you to simply scale workers horizontaly based on your needs.

### Getting Started
1. Make sure you have installed below requirements on your system:
```
docker
docker-compose
ssh-keygen
```

2. Copy .env_example to .env
```
$ cp env_example .env
```

3. If you have your own invetory and database server, please update .env with your variables. If you dont, leave it as it is and we are going to spin up test environment in next steps
```
$ cat .env
HOSTS_INVENTORY=http://issues-inventory:5000/inventory # YAML list of servers
SCHEDULE_INTERVAL=10s # issue read interval
ISSUE_FILE=/etc/issue # issue file location
REDIS=issues-redis # redis server used as broker between scheduler and workers
SSH_PRIVATE_KEY_FILE=/tmp/id_rsa # private keys
SSH_USER=issues # ssh user, used to connect to remote servers
SSH_PORT=2222 # ssh port, used to connect to remote servers
DB_NAME=issues # issues postgres database name
DB_HOST=issues-postgres # issues postgres host 
DB_USER=issues # issues postgres user
DB_PASSWORD=123456 # issues postgres password
POSTGRES_PASSWORD=123 # postgres admin password, only required in case you want provision new postgres server
```

4. Load vars
```
$ source .env
```

5. Build docker images
```
$ make build-images
```

6. Create test environment, this include 2 containers with ssh access and 1 web server which hosts the inventory
```
$ make create-test-env
```

7. Create postgres server and configure database, in case you do not have it
```
$ make create-postgres
```

8. Run the issues app, it will spin up 3 docker containers(redis, scheduler, worker)
```
$ make run
```

9. Verify db is update with issue content to confirm app is working. If output of below command is empty then something is wrong.
```
$ make query-db
('id', 'host', 'issue', 'updated')
(229, 'issues-ssh1', '', datetime.datetime(2022, 9, 14, 7, 34, 4, 237407))
(230, 'issues-ssh2', '', datetime.datetime(2022, 9, 14, 7, 34, 4, 408029))
```


#### ADVANCED USE:
To add more workers
```
$ docker run --name issue-worker1 issues-app celery -A issues.worker worker
$ docker run --name issue-worker2 issues-app celery -A issues.worker worker
```

To increase worker forks use --concurrency flag
```
$ docker run --name issue-worker1 issues-app celery -A issues.worker worker --concurrency=10
```
