from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
import pika
from decouple import config


# check of access token in cookies
def authenticate(function):
    def wrapper(self, request, *args, **kwargs):
        access_token = request.COOKIES.get('ACCESS_TOKEN')
        
        if access_token:
            try:
                user_detail = AccessToken(access_token)
                user_id = user_detail['user_id']
                if user_id:
                    kwargs['user_id'] = user_id
                    return function(self, request, *args, **kwargs)
            except Exception as e:
                # Token is invalid
                response = {"detail": "Invalid token"}
                return Response(response, status=401)
        
        # Token is not provided
        response = {"detail": "Authentication credentials were not provided."}
        return Response(response, status=401)

    return wrapper


# connect to rabbit mq
def connection(function):
    def wrapper(*args, **kwargs):
        connection = pika.BlockingConnection(pika.URLParameters(config('RABBITMQ')))
        channel = connection.channel()
        kwargs['channel'] = channel
        response = function(*args,**kwargs)
        connection.close()
        return response
    return wrapper
