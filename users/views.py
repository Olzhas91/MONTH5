import random

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import UserCode
from users.serializer import UserRegisterSerializer


@api_view(['POST'])
def register_api_view(request):
    serializer = UserRegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = User.objects.create_user(**serializer.validated_data, is_active=False)
    confirm = UserCode.objects.create(user=user, code=random.randint(100000, 999999))
    return Response ({'status': 'Пользователь зарегестрирован', 'code': confirm.code, 'data': serializer.data}, status=status.HTTP_201_CREATED)



