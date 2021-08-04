from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import CustomUser


class LoginForm(forms.Form):
    email = forms.CharField(max_length=64, label=False, widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password=  forms.CharField(max_length=64, label=False, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = CustomUser
        fields = ['email', 'password']


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=64, label=False, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    last_name = forms.CharField(max_length=64, label=False, widget=forms.TextInput(attrs={'placeholder': 'Surname'}))
    email = forms.CharField(max_length=64, label=False, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(max_length=64, label=False, required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=64, label=False, required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}))


    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email','password1', 'password2']

        def clean(self):
            email = super().clean().get('email')

            if '@' not in email:
                raise forms.ValidationError('Email doesnt have @')
