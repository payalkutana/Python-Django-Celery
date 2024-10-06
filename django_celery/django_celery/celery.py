import os
from celery import Celery
from time import sleep
from datetime import timedelta
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

app = Celery('django_celery')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(name="addition_task")
def add(x, y):
    sleep(20)
    return x + y

#METHOD 2 OF Scheduling Task
app.conf.beat_schedule = {
    'celery-config-task':{
        'task':'celery_app.tasks.second_schedule_task',
        'schedule':timedelta(seconds=20),
        'args':('11111', )
        # 'args':('second_task_called_from_celery.py', )
    }
}

# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')