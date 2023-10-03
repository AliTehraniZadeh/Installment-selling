from rest_framework import viewsets, status
from . import models, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly 
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return{
        'refresh' : str(refresh),
        'access' : str(refresh.access_token)
    }


class UserView(viewsets.ModelViewSet):
    queryset = models.UserModel.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]  # ایجاد سطح دسترسی


class ShopView(viewsets.ModelViewSet):
    queryset = models.ShopModel.objects.all()
    serializer_class = serializers.ShopSerializer


class BranchView(viewsets.ModelViewSet):
    queryset = models.BranchModel.objects.all()
    serializer_class = serializers.BranchSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer


class CheckView(viewsets.ModelViewSet):
    queryset = models.CheckModel.objects.all()
    serializer_class = serializers.CheckSerializer


class InstallmentViews(viewsets.ModelViewSet):
    queryset = models.InstallmentModel.objects.all()
    serializer_class = serializers.InstallmentSerializer