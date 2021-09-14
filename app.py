from celery import Celery

app = Celery('Calculator', broker='amqp://guest:guest@localhost:5672')

app.conf.task_default_exchange = 'Calculator'
app.conf.task_default_routing_key = 'Calculator'
app.conf.task_default_queue = 'Calculator'


@app.task()
def Calculator(a, operator , b):
    ch = operator

    if ch == '+':
        return a+b
    if ch == '-':
        return a-b
    if ch == '*':
        return a*b
    elif ch == '/':
        return a/b
    else :
        print("Invalid Operation")
    