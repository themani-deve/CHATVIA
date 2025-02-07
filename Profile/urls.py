from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('change-password/', views.change_password, name='change_password'),
    path('change-profile-photo/', views.change_profile_photo, name='change_profile_photo'),
    path('change-personal-information/', views.change_personal_information, name='change_personal_information'),
    path('change-api-token/', views.change_api_token, name='change_api_token'),
]
