from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path("", views.Users.as_view()),
    path("myinfo", views.MyInfo.as_view()),

    # Authentication
    path("getToken", obtain_auth_token), #DRF Token

    path("login", views.Login.as_view()), #Django Session Login
    path("logout", views.Logout.as_view()), #Django Session Logout

    # JWT Authentication
    path("login/jwt", views.JWTLogin.as_view()),
    path("login/jwt/info", views.UserDetailView.as_view()),

    # Simple JWT Authentication
    path("login/simpleJWT", TokenObtainPairView.as_view()),
    path("login/simpleJWT/refresh", TokenRefreshView.as_view()),
    path("login/simpleJWT/verify", TokenVerifyView.as_view()),
]

