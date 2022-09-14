from issues.modules.db import check_db_exist, check_table_exist, check_user_exist, create_db, create_user, grant_all_priv, create_table, connect_db
from issues.config import db_config as db_conf

table=db_conf["table"]
db=db_conf["database"]
user=db_conf["user"]
password=db_conf["password"]
columns = [
    "id SERIAL PRIMARY KEY",
    "ip VARCHAR(20)",
    "issue_content VARCHAR(10000)",
    "updated TIMESTAMP"
  ]

a_db_conf = {
  "user": "postgres",
  "password": db_conf["postgres_pass"],
  "database": "postgres",
  "host": db_conf["host"],
  "port": db_conf["port"]
}
con = connect_db(a_db_conf)
if not check_db_exist(con, db):
  create_db(con, db)
if not check_user_exist(con, user):
  create_user(con, user, password)
  grant_all_priv(con, db, user)

con = connect_db(db_conf)
if not check_table_exist(con, table):
  create_table(con, table, columns)
