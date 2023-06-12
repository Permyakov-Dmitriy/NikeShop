import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NikeShop.settings")
app = Celery("NikeShop")

app.conf.beat_schedule = {
    'run-task-every-minute': {
        'task': 'main.tasks.check_birth_day_task',
        'schedule': crontab(hour=1, minute=47),
    },
}

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

