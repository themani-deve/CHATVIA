from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path('main/chat-with-pos-neg/', views.chat_with_pos_neg, name='chat_with_pos_neg'),
    path('main/ml-process-pos-neg/', views.ml_process_pos_neg, name='ml_process_pos_neg'),
]
