from issues.config import app_config
broker_url = "redis://{}:6379/0".format(app_config["redis"])
task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
enable_utc = True
