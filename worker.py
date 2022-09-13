from issues.celery import app
from issues.modules import ssh, db
from issues.config import db_config as db_conf
from issues.config import ssh_config as ssh_conf
from issues.config import app_config as app_conf
from issues.modules.helper import get_request,load_yaml


@app.task
def create_worker_tasks():
 r = get_request(hosts_inventory)
 servers = load_yaml(r.text)
 for k in servers.keys():
  chain = update_issue.s(servers[k])
  chain()

@app.task
def worker_task(server):
    # read issue from remote
    conf = dict(config.ssh_config)
    conf["server"] = server["ip"]
    c = ssh.connect_remote_server(conf)
    data = ssh.read_remote_file(c, config.app_config["issue_file"])
    # update db with issue content
    con = db.connect_db(db_conf)
    rid = db.get_query(con, db_conf["table"], ["id"], {"ip":server["ip"]})
    if rid:
        update_data = {
            "issue_content": issue,
            "updated": helper.get_timestamp()
        }
        db.update_record(con, db_conf["table"], update_data, {"id":rid})
    else:
        insert_data = {
            "ip": server["ip"],
            "issue_content": issue,
            "updated": helper.get_timestamp()
        }
        db.insert_query(con, db_conf["table"], insert_data)
