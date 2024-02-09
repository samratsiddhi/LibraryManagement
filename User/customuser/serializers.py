from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only =  True)
    
    def validate(self, attrs):    
        email = attrs.get('email')
        password = attrs.get('password')    
        
        user = authenticate(self.context['request'],email = email , password = password)
          
              
        if user:
        
            refresh = RefreshToken.for_user(user=user)
            refresh_token = str(refresh)
            
            access = AccessToken.for_user(user = user)
            access_token = str(access)
            
            data = {
                "status" : True,
                "access_token" : access_token,
                "refresh_token" :  refresh_token
            }
        
            return data
        
        return {
            "status" : False,
            "detail" : "invalid credentials"
            }