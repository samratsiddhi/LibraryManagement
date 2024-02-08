from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

def authenticate(function):
    def wrapper(self, request, *args, **kwargs):
        access_token = request.COOKIES.get('ACCESS_TOKEN')
        
        if access_token:
            try:
                user_detail = AccessToken(access_token)
                user_id = user_detail['user_id']
                if user_id:
                    # Call the wrapped view function
                    return function(self, request, *args, **kwargs)
            except Exception as e:
                # Token is invalid
                response = {"detail": "Invalid token"}
                return Response(response, status=401)
        
        # Token is not provided
        response = {"detail": "Authentication credentials were not provided."}
        return Response(response, status=401)

    return wrapper
