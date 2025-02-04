from django.urls import path
from . import views

urlpatterns = [
    path('set-permission/', views.set_permission, name='set_permission_for_decoding'),
    path('find-user/', views.find_user_for_set_permission, name='find_user'),
    path('my-permissions/', views.my_permissions, name='my_permissions'),
    path('my-permissions/<username>/', views.chat_with_other_users_alphabet, name='use_other_user_alphabet'),
    path('main/use-other-user-alphabet-encryption-processing/', views.use_other_user_alphabet_processing, name='use_other_user_alphabet_processing'),
    path('remove-access/', views.remove_access, name='remove_access'),
    path('other-permissions/', views.other_users_permission, name='other_user_permission'),
]
