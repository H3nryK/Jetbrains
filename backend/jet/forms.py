from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Old Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        strip=False,
    )
    new_password1 = forms.CharField(
        label='New password',
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label='New Password Confirmation',
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        strip=False,
    )