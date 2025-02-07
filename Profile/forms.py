from django import forms
from Authentication.models import User


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(label='Current Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))
    password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'id': 'NewPassword',
    }))
    password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'id': 'ConfirmNewPassword',
    }))


class ChangePersonalInformationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'last_name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}),
        }
        labels = {
            'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email',
        }
