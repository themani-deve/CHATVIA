from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from Authentication.models import User
from Other_U_Processing.models import PermissionForDecodingModel
from Main.signals import is_logged_in
from utils.Encryption.main import encryption


# Create your views here.

@is_logged_in
def set_permission(request):
    permissions = PermissionForDecodingModel.objects.filter(user1=request.user).order_by('-id')[:3]
    context = {
        'permissions': permissions,
    }
    return render(request, 'Other_U_Processing/set_permission.html', context)


@is_logged_in
def find_user_for_set_permission(request):
    username = request.GET.get('user_name')
    user = User.objects.filter(username=username).first()
    if user:
        permission, created = PermissionForDecodingModel.objects.get_or_create(user1=request.user, user2=user)
        return JsonResponse({
            'status': 'success',
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'csrf': get_token(request)
        })
    else:
        return JsonResponse({
            'status': 'error',
            'message': f'{username} does not exist!'
        })


@is_logged_in
def my_permissions(request):  # My Self Permission To Other Users
    permissions = PermissionForDecodingModel.objects.filter(user2=request.user)
    context = {
        'permissions': permissions,
    }
    return render(request, 'Other_U_Processing/my_permissions.html', context)


@is_logged_in
def other_users_permission(request):  # Other Users Permission To My Alphabet
    permissions = PermissionForDecodingModel.objects.filter(user1=request.user)
    context = {
        'permissions': permissions,
    }
    return render(request, 'Other_U_Processing/other_permission.html', context)


def chat_with_other_users_alphabet(request, username):
    user: User = User.objects.filter(username=username).first()
    permission = PermissionForDecodingModel.objects.filter(user1=user, user2=request.user).first()
    if permission:
        return render(request, 'Other_U_Processing/chat_with_user_alphabet.html')
    else:
        return render(request, 'Other_U_Processing/access_denied.html')


@is_logged_in
def use_other_user_alphabet_processing(request):
    username = request.POST.get('username')
    text = request.POST.get('text')
    user: User = User.objects.filter(username=request.user).first()
    if user:
        permissions = PermissionForDecodingModel.objects.filter(user1__username=username, user2=user).first()
        if permissions:
            user_alphabet: User = User.objects.filter(username=username).first()
            encryption_result = encryption(text=text, alphabet_dict=user_alphabet.get_alphabet_dict())
            return JsonResponse({
                'y_pred': encryption_result,
            })
        else:
            return JsonResponse({
                'y_pred': 'Access Denied!',
            })
    else:
        return JsonResponse({
            'y_pred': 'User Not Found!',
        })


@is_logged_in
def remove_access(request):
    username = request.POST.get('username')
    permission: PermissionForDecodingModel = PermissionForDecodingModel.objects.filter(user2__username=username).first()
    try:
        if permission:
            permission.delete()
            return JsonResponse({
                'response': 'Success!'
            })
    except Exception as e:
        print(f'Error Message is: {e}')
