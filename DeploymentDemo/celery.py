import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DeploymentDemo.settings")

app = Celery("DeploymentDemo")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()