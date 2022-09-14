from paramiko import SSHClient, AutoAddPolicy

def connect_remote_server(config):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(config["server"], port=config["port"], username=config["user"], key_filename=config["key_file"])
    return client

def read_remote_file(client, file):
	stdin, stdout, stderr = client.exec_command("cat {}".format(file))
	content = stdout.read().decode("utf8")
	stdin.close()
	stdout.close()
	stderr.close()
	return content
