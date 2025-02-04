from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, reverse
from Authentication.models import User
from Authentication.forms import *
from utils.Encryption.create_ascii import generate_alphabet_dict


# Create your views here.


def register_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('main'))
    else:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user_email = form.cleaned_data['email']
                user_pass = form.cleaned_data['password']
                user: User = User.objects.filter(email=user_email).first()
                if user:
                    form.add_error('email', 'Email Does Exists!!!')
                else:
                    split_email_for_username = user_email.lower().split('@')
                    str_split = ''.join(split_email_for_username[0])
                    new_user = User(username=str_split, email=user_email, is_active=True)
                    alphabet_dict = generate_alphabet_dict()
                    new_user.set_alphabet_dict(alphabet_dict)
                    new_user.set_password(user_pass)
                    new_user.save()
                    return redirect(reverse('login'))
        context = {
            'form': form,
        }
        return render(request, 'Authentication/register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('main'))
    else:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user_email = form.cleaned_data['email']
                user_pass = form.cleaned_data['password']
                user: User = User.objects.filter(email=user_email).first()
                if user:
                    if user.check_password(user_pass):
                        login(request, user)
                        if user.alphabet_dict is None:
                            alphabet_dict = generate_alphabet_dict()
                            user.set_alphabet_dict(alphabet_dict)
                        request.session['alphabet_dict'] = user.get_alphabet_dict()
                        return redirect(reverse('main'))
                    else:
                        form.add_error('password', 'Password is Not Correct!!!')
                else:
                    form.add_error('email', 'Email Not Exists!!!')
        context = {
            'form': form,
        }
        return render(request, 'Authentication/login.html', context)


def forgot_pass_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('main'))
    else:
        form = ForgotPassForm()
        if request.method == 'POST':
            form = ForgotPassForm(request.POST)
            if form.is_valid():
                user_email = form.cleaned_data['email']
                user: User = User.objects.filter(email=user_email).first()
                if user:
                    # todo: Send Forgot Password Email!!!
                    return redirect(reverse('login'))
                else:
                    form.add_error('email', 'Email Does Not Exists!!!')
        context = {
            'form': form,
        }
        return render(request, 'Authentication/forgot_password.html', context)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(reverse('login'))
    else:
        return redirect(reverse('main'))
