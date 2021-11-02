from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import AccessToken

from ..permissions import IsAdmin
from ..serializers.user import (CustomUserSerializer, EmailSerializer,
                                UserRegistrationSerializer)

User = get_user_model()


def send_message(email, code):
    subject = 'Confirmation code'
    body = f'''
        {code}
    '''
    send_mail(
        subject, body,
        from_email=EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=True,
    )


@api_view(['POST'])
def email_request(request):
    serializer = EmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data['email']
    username = serializer.data['username']
    user = User.objects.get_or_create(
        email=email,
        username=username,
    )
    confirmation_code = default_token_generator.make_token(user)
    send_message(email, confirmation_code)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_token(request):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data['email']
    code = serializer.data['confirmation_code']
    user = get_object_or_404(User, email=email)
    if default_token_generator.check_token(user, code):
        access_token = AccessToken.for_user(user)
        return Response(
            {'token': f'{access_token}'},
            status=status.HTTP_200_OK,
        )
    return Response(
        {'token': 'Invalid authorization token'},
        status=status.HTTP_400_BAD_REQUEST,
    )


class CustomUserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdmin]
    lookup_field = 'username'
    filter_backends = [DjangoFilterBackend]
    search_fields = ['username']

    @action(
        detail=False,
        methods=['GET', 'PATCH'],
        permission_classes=[IsAuthenticated]
    )
    def me(self, request):
        if request.method == 'GET':
            return Response(
                self.get_serializer(request.user).data,
                status=status.HTTP_200_OK,
            )
        serializer = self.get_serializer(
            request.user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(role=request.user.role)
        return Response(serializer.data, status=status.HTTP_200_OK)
