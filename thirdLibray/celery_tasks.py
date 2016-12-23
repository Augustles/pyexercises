# coding=utf-8

from celery import Celery

# 任务队列
# 启动celery -A celery_task worker --logevel=info
# from celery_tasks import add
# result = add.delay(5,4)
# if not result.traceback: # 如果没有错误返回
# print result.get()
# 如果有错误可以用 result.traceback

app = Celery('tasks', backend='redis://localhost', broker='redis://localhost')

@app.task
def add(x, y):
    return x+y
