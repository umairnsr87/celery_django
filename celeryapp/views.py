from django.shortcuts import render
from .tasks import *
# from celery import Celery
# from time import sleep
# app = Celery('tasks', broker='redis://localhost:6379/0')
#
# @app.task
# def add(x, y):
#     sleep(10)
#     return x + y
#
# @app.task
# def reverse(string):
#     sleep(5)
#     return string[::-1]
#
# @app.task
# def addtostring(x):
#     return x+"added"

# Create your views here.

def home(request):
    add_val=add.delay(2, 4)
    mul_val=mul.delay(2,8)
    x_sum=xsum.delay([add_val.get(),mul_val.get()])
    # for i in range(100):
    #     print(i)

    print(x_sum.get(),add_val.get(),mul_val.get())


    # add.delay(2,4)
    # addtostring("kitty")
    # reverse("kiddo")
    return render(request,'home.html',{})
