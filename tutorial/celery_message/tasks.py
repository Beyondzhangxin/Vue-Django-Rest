# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def add(x, y):
    pass


@shared_task
def mul(x, y):
    pass


@shared_task
def xsum(numbers):
    pass