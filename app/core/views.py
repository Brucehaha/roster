from django.shortcuts import render, HttpResponse, redirect
from django.utils.timezone import datetime
# Create your views here.
from celery.result import AsyncResult
from .tasks import add


def celery_res(request):
    task_id = 'bcc9ad18-736f-40ea-97cb-eeb23fd99a79'
    res = AsyncResult(id=task_id)
    return HttpResponse(res.get())


def celery_test(request):
    task = add.delay(4, 22)
    # res = task.get()
    print('ddddd', task)
    return HttpResponse(task.id)
