import pika, sys, os
import json
from django.core.wsgi import get_wsgi_application
from decouple import config

# Set the DJANGO_SETTINGS_MODULE dynamically based on script location

script_path = os.path.abspath(__file__)
project_path = os.path.dirname(os.path.dirname(script_path))
sys.path.append(project_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Borrower.settings")

# Initialize Django
application = get_wsgi_application()

from booklog.models import Booklog
from django.core.exceptions import ObjectDoesNotExist

connection = pika.BlockingConnection(pika.URLParameters(config('RABBITMQ')))
channel = connection.channel()


channel.queue_declare(queue= "borrow_book_with_id")
channel.exchange_declare(exchange= "borrow_book_exhange", exchange_type="direct")  

channel.queue_bind(queue= "borrow_book_with_id",
                   exchange="borrow_book_exhange",
                    routing_key="borrow_book_route",
                   )

# def main():
def callback(ch, method, properties, body): 
        received_message_str = body.decode('utf-8')
        message_dict = json.loads(received_message_str)
        
        print("recieved : ", message_dict)
        book_id = message_dict['book_id']
        user_id = message_dict['user_id']
        try:
            log = Booklog.objects.get(user_id=user_id)
            log.book_id.append(book_id)
            log.save()
        except ObjectDoesNotExist:
            Booklog.objects.create(user_id=user_id, book_id=[book_id])
            
        
channel.basic_consume(queue='borrow_book_with_id', on_message_callback=callback, auto_ack=True)
    
print("consuming......")  
channel.start_consuming()


# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         print('Interrupted')
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)
    

