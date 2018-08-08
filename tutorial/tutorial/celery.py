# coding:utf-8
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# 获取当前文件夹名，即为该Django的项目名
project_name = os.path.split(os.path.abspath('.'))[-1]
project_settings = '%s.settings' % project_name

# set the default Django settings module for the 'celery' program.设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', project_settings)

# 实例化Celery
app = Celery(project_name)

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')
# 使用django的settings文件配置celery
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
# Celery加载所有注册的应用
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


