from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from Authentication.models import User
from Profile.forms import ChangePasswordForm
from rest_framework.authtoken.models import Token
from Main.signals import is_logged_in
from Profile.forms import ChangePersonalInformationForm


# Create your views here.

@is_logged_in
def profile_view(request):
    token: Token = Token.objects.filter(user_id=request.user.id).last()
    context = {
        'token': token,
    }
    return render(request, 'Profile/profile.html', context)


@is_logged_in
def delete_account(request):
    user_id = request.POST.get('user_id')
    print(request.POST)
    user: User = User.objects.filter(id=user_id).first()
    if user:
        user.delete()
        return redirect(reverse('login'))


@is_logged_in
def change_password(request):
    form = ChangePasswordForm()
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_password = form.cleaned_data['current_password']
            new_password = form.cleaned_data['password1']
            user: User = User.objects.filter(id=request.user.id).first()
            if user:
                if user.check_password(current_password):
                    user.set_password(new_password)
                    user.save()
                    return redirect(reverse('login'))
                else:
                    form.add_error('current_password', 'Current Password is Not Correct!')
            else:
                return redirect(reverse('login'))
    context = {
        'form': form,
    }
    return render(request, 'Profile/change_password.html', context)


@is_logged_in
def change_api_token(request):
    token: Token = Token.objects.filter(user_id=request.user.id).all().delete()
    new_token = Token.objects.create(user=request.user)
    new_token.save()
    return JsonResponse({
        'new_token': new_token.key,
    })


@is_logged_in
def change_profile_photo(request):
    return render(request, 'Profile/change_profile_photo.html')


@is_logged_in
def change_personal_information(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePersonalInformationForm(request.POST, instance=user)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile')
    else:
        form = ChangePersonalInformationForm(instance=user)
    context = {
        'form': form,
    }
    return render(request, 'Profile/change_personal_information.html', context)
