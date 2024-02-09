import pika
from decouple import config

connection = pika.BlockingConnection(pika.URLParameters(config('RABBITMQ')))
channel = connection.channel()
channel.queue_declare(queue= "borrow_book")

def publish(message):
    try:
        channel.queue_declare(queue= "borrow_book")

        channel.basic_publish(exchange="",
                              routing_key="borrow_book",
                              body=message)
        print("connection successful")
        connection.close()
    except Exception as e:
        print(e)
        
    print("message sent =  ", message)
