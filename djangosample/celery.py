import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangosample.settings')

app = Celery('djangosample')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
