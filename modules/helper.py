from datetime import datetime, timezone
import requests, yaml


def get_request(url):
	return requests.get(url)

def load_yaml(s):
	return yaml.safe_load(s)

def get_timestamp():
	return datetime.now(timezone.utc)

def convert_to_seconds(t):
	if t[-1] == 's':
		s = t[:-1]
	elif t[-1] == 'm':
		s = t[:-1]*60
	elif t[-1] == 'h':
		s = t[:-1]*60*60
	elif t[-1] == 'd':
		s = t[:-1]*60*60*24
	else: 
		s = 0 
	return int(s)

