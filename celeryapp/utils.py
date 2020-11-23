from celery import Celery
from time import sleep
app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def add(x, y):
    sleep(10)
    return x + y

@app.task
def reverse(string):
    sleep(5)
    return string[::-1]

@app.task
def addtostring(x):
    return x+"added"