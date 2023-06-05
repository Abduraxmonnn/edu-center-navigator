# Python
import os

# Celery
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# CELERY beat tasks

app.conf.beat_schedule = {
    'send_mailing_every_14_days': {
        'task': 'apps.main.news.tasks.py',
        'schedule': crontab(minute='*/1')
    }
}
