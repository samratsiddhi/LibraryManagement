from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from django.conf import settings


# Create your views here.
class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        data = serializer.validated_data
        response = Response()
        
        response.set_cookie(
            key = 'REFRESH_TOKEN',
            value = (data['refresh_token']),
            samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
            expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            secure = False,
            httponly= True,
        )
        
        response.set_cookie(
            key = 'ACCESS_TOKEN',
            value = (data['access_token']),
            samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
            expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            secure = False,
            httponly= True,
        )
        
        response.data = {
            'status' : 'successful login',
            'data' : data
        }
        return response