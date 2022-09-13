import yaml
from flask import Flask
from issues.config import test_config

app = Flask(__name__)

@app.route("/inventory", methods=["GET"])
def get_servers_list():
    servers = []
    with open(test_config["mock_inventory"], 'r') as f:
        servers = yaml.safe_load(f)
    return yaml.dump(servers)

if __name__ == "__main__":
    app.run()