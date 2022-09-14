from __future__ import absolute_import, unicode_literals
from celery import Celery
import os
import environ
from pathlib import Path
from django.conf import settings

path = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(env_file=os.path.join(path, ".env"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      f'nightlab_backend.settings.{env("django_env")}')

app = Celery("nightlab_backend")
app.conf.enable_utc = False
app.conf.update(timezone="Asia/Kolkata")

app.config_from_object(settings, namespace="CELERY")

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
