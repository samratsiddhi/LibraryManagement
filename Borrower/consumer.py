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
connection = pika.BlockingConnection(pika.URLParameters(config('RABBITMQ')))
channel = connection.channel()
channel.queue_declare(queue= "borrow_book")

def main():
    def callback(ch, method, properties, body):
        print("consumed something")
        message = body.decode('utf-8')
        book_id = message['book_id']
        print("book_id : " , book_id)
        
    channel.basic_consume(queue='borrow_book', on_message_callback=callback, auto_ack=True)
    
    print("consuming......")  
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    

