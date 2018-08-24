# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

from celery import Celery

app=Celery('tasks',broker='redis://123.56.235.47:8200/0')


@app.task()
def add(x,y):
    return x+y

@shared_task
def add(x, y):
    pass


@shared_task
def mul(x, y):
    pass


@shared_task
def xsum(numbers):
    pass