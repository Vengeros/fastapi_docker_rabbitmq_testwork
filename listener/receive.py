import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
channel = connection.channel()

channel.queue_declare(queue='task_queue')

print('[*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(body, file=sys.stdout)

channel.basic_consume(on_message_callback=callback, queue='task_queue')

channel.start_consuming()