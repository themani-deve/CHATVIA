from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path('ml-process/', views.ml_process, name='ml_process'),
]
