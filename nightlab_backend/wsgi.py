import os
from django.core.wsgi import get_wsgi_application
import environ
from pathlib import Path

path = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(env_file=os.path.join(path, ".env"))


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      f'nightlab_backend.settings.{env("django_env")}')

application = get_wsgi_application()
