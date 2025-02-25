from rest_framework.authentication import BaseAuthentication
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.conf import settings

User = get_user_model()

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        if not request.headers:
            return None

        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None
        
        if not auth_header.startswith('Bearer'):
            raise AuthenticationFailed('Auth header not a valid bearer token')
        
        token = auth_header.replace('Bearer ', '')
        
        try:
            payload = jwt.decode(
                jwt=token, 
                key=settings.SECRET_KEY,
                algorithms=['HS256']
            )

            # Search for the user id that was inside the token
            user = User.objects.get(id=payload['user']['id'])

            return (user, token)
        except Exception as e:
            print(e)
            raise AuthenticationFailed('Invalid credentials provided')