from django.contrib.auth import get_user_model, logout
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.translation import gettext_lazy as _

from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from authx.permissions import IsOwnerUser
from .serializers import UserSerializer


User = get_user_model()


class UserViewSet(ModelViewSet):
    """ViewSet of User model"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerUser]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        logout(request)
        self.perform_destroy(instance)
        return Response(status=HTTP_204_NO_CONTENT)

    def send_auth_email(self, user):
        """Returns email activation for new registered user"""
        current_site = get_current_site(self.request)
        domain = current_site.domain
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        mail_subject = _('Activate your account')
        protocol = 'http'

        url = f"{protocol}://{domain[0]}/rest-api/v1/authx/activate/{uid[0]}/{token}"
        message = f'<p><a href="{url}">{url}</a></p>'

        email = EmailMessage(mail_subject, message, to=[user.email])
        email.send()

    def perform_create(self, serializer):
        user = serializer.save()
        user.is_active = False
        user.save()
        self.send_auth_email(user)
