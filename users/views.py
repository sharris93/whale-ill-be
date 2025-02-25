from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotAuthenticated, ValidationError
from django.contrib.auth import get_user_model
from .serializers.common import UserSerializer
import jwt
from django.conf import settings
from datetime import datetime, timedelta

User = get_user_model()


# /auth/register/
class RegisterView(APIView):

    def post(self, request):
        serialized_user = UserSerializer(data=request.data)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response(serialized_user.data, 201)
        return Response(serialized_user.errors, 422)
    

# /auth/login/
class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            # 1. Search for the user by its username
            user = User.objects.get(username=username)

            # 2. Check plain text password matches hash, raise validation error if not
            if not user.check_password(password):
                raise ValidationError({ 'password': 'Passwords do not match' })
            
            # 3. Generate an expiry date
            exp_date = datetime.now() + timedelta(days=1)

            # Generate token using pyjwt package
            token = jwt.encode(
                payload={
                    'user': {
                        'id': user.id,
                        'username': user.username,
                        'profile_image': user.profile_image,
                        'is_admin': user.is_staff
                    },
                    'exp': int(exp_date.strftime('%s'))
                },
                key=settings.SECRET_KEY,
                algorithm='HS256'
            )

            # Send token in response
            return Response({ 'message': 'Login was successful', 'token': token })
            
        except (User.DoesNotExist, ValidationError) as e:
            # If either a DoesNotExist or a ValidationError is raised inside the catch, this except block will catch it
            print(e)
            raise NotAuthenticated('Invalid credentials')