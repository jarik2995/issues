from celery import Celery
from issues.modules.helper import convert_to_seconds
from issues.config import app_config as app_conf

app = Celery('issues',
 include=['issues.worker'])
app.config_from_object('issues.celeryconfig')
app.conf.beat_schedule = {
 'issues schedule': {
 'task': 'issues.worker.create_worker_tasks',
 'schedule': convert_to_seconds(app_conf["schedule_interval"])
 }
}
