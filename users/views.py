
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer


# Регистрация
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


# Вход в аккаунт
class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]


# Обновление токена
from rest_framework_simplejwt.views import TokenRefreshView


class RefreshTokenView(TokenRefreshView):
    permission_classes = [AllowAny]


# Выход из аккаунта
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {'message': 'Вы успешно вышли из аккаунта'},
                status=status.HTTP_200_OK
            )

        except Exception:
            return Response(
                {'error': 'Недействительный токен'},
                status=status.HTTP_400_BAD_REQUEST
            )
