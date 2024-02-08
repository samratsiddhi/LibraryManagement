import pika
from decouple import config

connection = pika.BlockingConnection(pika.URLParameters(config('RABBITMQ')))
channel = connection.channel()

def publish(message):
    try:
        print("connection successful")
        connection.close()
    except Exception as e:
        print(e)
        
    print("message=", message)
