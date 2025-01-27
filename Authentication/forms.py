from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='Email', widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg border-light bg-light-subtle', 'placeholder': 'Enter Email',
        }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg border-light bg-light-subtle', 'placeholder': 'Enter Password',
    }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg border-light bg-light-subtle', 'placeholder': 'Enter Password',
    }))

    def clean_password2(self):
        pass1 = self.cleaned_data.get('password')
        pass2 = self.cleaned_data.get('password2')

        if pass1 == pass2:
            return pass1
        else:
            raise ValidationError('Password And Confirm Password Not Match!!!')


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email', widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg border-light bg-light-subtle', 'placeholder': 'Enter Email',
        }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg border-light bg-light-subtle', 'placeholder': 'Enter Password',
    }))


class ForgotPassForm(forms.Form):
    email = forms.EmailField(
        label='Email', widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg border-light bg-light-subtle', 'placeholder': 'Enter Email',
        }))
