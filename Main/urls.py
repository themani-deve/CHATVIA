from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path('main/chat-with-pos-neg/', views.chat_with_pos_neg, name='chat_with_pos_neg'),
    path('main/ml-process-pos-neg/', views.ml_process_pos_neg, name='ml_process_pos_neg'),
    path('main/chat-with-encryption/', views.chat_with_encryption, name='chat_with_encryption'),
    path('main/encryption-processing/', views.encryption_processing, name='encryption_processing'),
    path('main/chat-with-decoder/', views.chat_with_decoder, name='chat_with_decoder'),
    path('main/decoder-processing/', views.decoder_processing, name='decoder_processing'),
]
