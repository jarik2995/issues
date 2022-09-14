from issues.modules.db import connect_db, get_all
from issues.config import db_config as db_conf

table=db_conf["table"]
db=db_conf["database"]
user=db_conf["user"]
password=db_conf["password"]

con = connect_db(db_conf)
print(("id","host","issue","updated"))
for r in get_all(con, "host_issues", ["*"]):
    print(r)
