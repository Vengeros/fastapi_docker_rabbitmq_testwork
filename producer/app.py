from fastapi import Body, FastAPI, status
import pika
from time import sleep
from schemas import Task


app = FastAPI()

connection = None
while True:
    try:
        sleep(5)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
        break
    except:
        pass
channel = connection.channel()


@app.on_event("startup")
async def startup():
    channel.queue_declare(queue='task_queue')


@app.on_event("shutdown")
async def shutdown():
    connection.close()


@app.post('/add_task', status_code=status.HTTP_201_CREATED,)
def hello(task: Task = Body(..., title='The phone number to be checked')):
    channel.basic_publish(exchange='', routing_key='task_queue', body=task.to_string())
