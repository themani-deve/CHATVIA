from django.urls import path
from . import views

urlpatterns = [
    path('set-permission/', views.set_permission, name='set_permission'),
    path('find-user/', views.find_user_for_set_permission, name='find_user'),
    path('my-permissions/', views.my_permissions, name='my_permissions'),
    path('my-permissions/encryption/<username>/', views.chat_with_other_users_alphabet_encryption, name='use_other_user_alphabet_encryption'),
    path('my-permissions/decoding/<username>/', views.chat_with_other_users_alphabet_decoding, name='use_other_user_alphabet_decoding'),
    path('main/use-other-user-alphabet-encryption-processing/', views.use_other_user_alphabet_encryption_processing, name='use_other_user_alphabet_encryption_processing'),
    path('main/use-other-user-alphabet-decoding-processing/', views.use_other_user_alphabet_decoding_processing, name='use_other_user_alphabet_decoding_processing'),
    path('remove-access/', views.remove_access, name='remove_access'),
    path('other-permissions/', views.other_users_permission, name='other_user_permission'),
]
