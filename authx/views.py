from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from .jwt import create_jwt, decode_jwt
from datetime import datetime, timedelta


User = get_user_model()


class LoginView(APIView):
    authentication_classes = []
    permission_classes = []
    # parser_classes = (JSONParser,)

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("User not found!")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")

        payload = {
            'id': user.id,
            'exp': datetime.utcnow() + timedelta(minutes=60),
            'iat': datetime.utcnow(),
        }
        token = create_jwt(payload)
        return Response({'jwt': token})
