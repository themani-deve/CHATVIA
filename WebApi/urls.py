from django.urls import path
from . import views
from rest_framework.authtoken import views as token

urlpatterns = [
    path('api/pos-nev/', views.PosNevApi.as_view()),
    path('api-token-auth/', token.obtain_auth_token),
]
