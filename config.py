from os import getenv


app_config = {
	"schedule_interval": getenv("SCHEDULE_INTERVAL", "10s"),
	"hosts_inventory": getenv("HOSTS_INVENTORY", "http://127.0.0.1:5000/inventory"),
	"issue_file": getenv("ISSUE_FILE", "/etc/issue")
}

ssh_config = {
	"key_file": getenv("SSH_PRIVATE_KEY_FILE", "/tmp/id_rsa"),
	"user": getenv("SSH_USER", "issues"),
	"port": getenv("SSH_PORT", "22")
}
db_config = {
	"user": getenv("DB_USER", "issues"),
	"password": getenv("DB_PASSWORD", "123"),
	"database": getenv("DB_NAME", "issues"),
	"port": getenv("DB_PORT", "5432"),
	"host": getenv("DB_HOST", "localhost"),
	"table": getenv("DB_TABLE", "host_issues")
}


