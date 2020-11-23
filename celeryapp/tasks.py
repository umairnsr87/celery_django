from celery import shared_task
from  time import  sleep


@shared_task
def add(x, y):
    sleep(10)
    return x + y


@shared_task
def mul(x, y):
    sleep(20)
    return x * y


@shared_task
def xsum(numbers):
    sleep(10)
    return sum(numbers)