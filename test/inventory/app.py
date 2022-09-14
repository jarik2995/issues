import yaml
from flask import Flask

app = Flask(__name__)

@app.route("/inventory", methods=["GET"])
def get_servers_list():
    servers = []
    with open("/tmp/servers_inventory.yaml", "r") as f:
        servers = yaml.safe_load(f)
    return yaml.dump(servers)

if __name__ == "__main__":
    app.run()
