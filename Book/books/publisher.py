import json
import pika
from decouple import config
from .decorators import connection

@connection
def publish(message,channel):
    try:
        # connection = pika.BlockingConnection(pika.URLParameters(config('RABBITMQ')))
        # channel = connection.channel()
        channel.queue_declare(queue= "borrow_book_with_id")  
        channel.exchange_declare(exchange= "borrow_book_exhange", exchange_type="direct")  
        channel.basic_publish(exchange="borrow_book_exhange",
                              routing_key="borrow_book_route",
                              body=json.dumps(message))
        # connection.close()
    except Exception as e:
        print(e)    
        
    print("message sent =  ", message)

# def return_book(message):
#     try:
#         connection = pika.BlockingConnection(pika.URLParameters(config('RABBITMQ')))
#         channel = connection.channel()
#         channel.queue_declare(queue= "borrow_book_with_id")  
#         channel.exchange_declare(exchange= "borrow_book_exhange", exchange_type="direct")  
#         channel.basic_publish(exchange="borrow_book_exhange",
#                               routing_key="borrow_book_route",
#                               body=json.dumps(message))
#         connection.close()
#     except Exception as e:
#         print(e)    
        
#     print("message sent =  ", message)
